import { test, expect } from '@playwright/test';
import { config } from '../../src/config/env';
import { loadOpenApi, hasOperation, EventHubApi } from '../../src/api/eventhub-api';

test('documented public API read operation and EventHub login UI are both reachable', async ({ request, page }) => {
  test.skip(!config.openApiSpecUrl || !config.publicGetPath, 'Configure actual OpenAPI JSON URL and public GET path.');
  const spec = await loadOpenApi(request);
  expect(hasOperation(spec, config.publicGetPath, 'GET')).toBeTruthy();
  const response = await new EventHubApi(request).get(config.publicGetPath);
  expect(response.status()).toBeLessThan(500);

  await page.goto(config.loginPath);
  await expect(page.locator('input[type="email"]').first()).toBeVisible();
});
