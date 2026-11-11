import { APIRequestContext, APIResponse, expect } from '@playwright/test';
import { config, parseJsonEnv } from '../config/env';

export interface OpenApiDocument {
  openapi?: string;
  swagger?: string;
  info?: { title?: string; version?: string };
  paths?: Record<string, Record<string, unknown>>;
}

export async function loadOpenApi(request: APIRequestContext): Promise<OpenApiDocument> {
  if (!config.openApiSpecUrl) throw new Error('Set OPENAPI_SPEC_URL to the exact OpenAPI JSON URL from Swagger.');
  const response = await request.get(config.openApiSpecUrl, { headers: { Accept: 'application/json' } });
  expect(response.ok(), `OpenAPI JSON returned HTTP ${response.status()}; verify OPENAPI_SPEC_URL.`).toBeTruthy();
  const spec = await response.json() as OpenApiDocument;
  expect(Boolean(spec.openapi || spec.swagger), 'Document must be OpenAPI or Swagger JSON').toBeTruthy();
  expect(Object.keys(spec.paths ?? {}).length, 'OpenAPI document must contain paths').toBeGreaterThan(0);
  return spec;
}

export function hasOperation(spec: OpenApiDocument, path: string, method: string): boolean {
  return Boolean(spec.paths?.[path]?.[method.toLowerCase()]);
}

export function listOperations(spec: OpenApiDocument) {
  const supported = new Set(['get', 'post', 'put', 'patch', 'delete', 'options', 'head']);
  return Object.entries(spec.paths ?? {}).flatMap(([path, item]) =>
    Object.entries(item).filter(([method, operation]) =>
      supported.has(method.toLowerCase()) && Boolean(operation) && typeof operation === 'object'
    ).map(([method, operation]) => ({ path, method: method.toUpperCase(), operation }))
  );
}

export function jsonPath(value: unknown, path: string): unknown {
  return path.split('.').filter(Boolean).reduce<unknown>((current, key) => {
    if (!current || typeof current !== 'object') return undefined;
    return (current as Record<string, unknown>)[key];
  }, value);
}

export class EventHubApi {
  constructor(private readonly request: APIRequestContext) {}
  private headers() {
    return {
      Accept: 'application/json',
      ...(config.apiToken ? { Authorization: `Bearer ${config.apiToken}` } : {})
    };
  }
  async send(method: string, path: string, data?: unknown): Promise<APIResponse> {
    const url = /^https?:\/\//i.test(path) ? path : `${config.apiBaseUrl}/${path.replace(/^\/+/, '')}`;
    return this.request.fetch(url, {
      method,
      headers: { ...this.headers(), ...(data === undefined ? {} : { 'Content-Type': 'application/json' }) },
      ...(data === undefined ? {} : { data })
    });
  }
  async get(path: string) { return this.send('GET', path); }
  async post(path: string, data: unknown) { return this.send('POST', path, data); }
}
