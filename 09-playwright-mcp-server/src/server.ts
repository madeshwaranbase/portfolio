import 'dotenv/config';
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { CallToolRequestSchema, ListToolsRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import { chromium, Browser, Page } from 'playwright';
import fs from 'node:fs/promises';
import path from 'node:path';

const allowedOrigin = process.env.MCP_ALLOWED_ORIGIN ?? 'https://eventhub.rahulshettyacademy.com';
const artifactDir = path.resolve(process.env.MCP_ARTIFACT_DIR ?? './artifacts');
let browser: Browser | undefined;
let page: Page | undefined;

async function currentPage(): Promise<Page> {
  browser ??= await chromium.launch({ headless: true });
  page ??= await browser.newPage();
  return page;
}
function allowedUrl(pathname: string): string {
  if (!['/','/login','/events','/bookings'].includes(pathname)) {
    throw new Error('Navigation path is not allow-listed.');
  }
  return new URL(pathname, allowedOrigin).toString();
}
const server = new Server(
  { name:'eventhub-playwright-mcp', version:'1.0.0' },
  { capabilities:{ tools:{} } }
);
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools:[
    {name:'open_eventhub',description:'Open an allow-listed EventHub page.',
     inputSchema:{type:'object',properties:{path:{type:'string',enum:['/','/login','/events','/bookings']}},required:['path']}},
    {name:'inspect_page',description:'Return current URL, title and visible headings.',
     inputSchema:{type:'object',properties:{}}},
    {name:'click_test_id',description:'Click a visible element by data-testid.',
     inputSchema:{type:'object',properties:{testId:{type:'string'}},required:['testId']}},
    {name:'fill_label',description:'Fill a form control by accessible label.',
     inputSchema:{type:'object',properties:{label:{type:'string'},value:{type:'string'}},required:['label','value']}},
    {name:'screenshot',description:'Save a screenshot in the local artifact directory.',
     inputSchema:{type:'object',properties:{fileName:{type:'string'}},required:['fileName']}}
  ]
}));
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  try {
    const p = await currentPage();
    const args = request.params.arguments ?? {};
    switch (request.params.name) {
      case 'open_eventhub': {
        const url = allowedUrl(String(args.path));
        await p.goto(url);
        return {content:[{type:'text',text:`Opened ${p.url()}`}]};
      }
      case 'inspect_page': {
        const headings = await p.locator('h1,h2,h3').allTextContents();
        return {content:[{type:'text',text:JSON.stringify({url:p.url(),title:await p.title(),headings},null,2)}]};
      }
      case 'click_test_id': {
        const id = String(args.testId ?? '');
        if (!/^[A-Za-z0-9_-]{1,80}$/.test(id)) throw new Error('Invalid test ID.');
        await p.getByTestId(id).click();
        return {content:[{type:'text',text:`Clicked ${id}`}]};
      }
      case 'fill_label': {
        const label = String(args.label ?? '');
        if (!label || label.length > 120) throw new Error('Invalid accessible label.');
        await p.getByLabel(label).fill(String(args.value ?? ''));
        return {content:[{type:'text',text:'Field filled.'}]};
      }
      case 'screenshot': {
        const fileName = String(args.fileName ?? 'eventhub.png');
        if (!/^[A-Za-z0-9_-]+\\.png$/.test(fileName)) throw new Error('Filename must be a simple PNG name.');
        await fs.mkdir(artifactDir,{recursive:true});
        const target = path.join(artifactDir,fileName);
        await p.screenshot({path:target,fullPage:true});
        return {content:[{type:'text',text:`Screenshot saved to ${target}`}]};
      }
      default: throw new Error(`Unsupported tool: ${request.params.name}`);
    }
  } catch (error) {
    return {isError:true,content:[{type:'text',text:error instanceof Error ? error.message : String(error)}]};
  }
});
await server.connect(new StdioServerTransport());
