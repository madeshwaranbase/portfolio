import { test, expect } from '@playwright/test';
import { config } from '../../src/config/env';
import { loadOpenApi, hasOperation, EventHubApi } from '../../src/api/eventhub-api';

test('configured public GET operation is documented and returns a non-server-error response', async ({ request }) => {
  test.skip(!config.openApiSpecUrl || !config.publicGetPath, 'Configure OPENAPI_SPEC_URL and API_PUBLIC_GET_PATH from Swagger.');
  const spec = await loadOpenApi(request);
  expect(hasOperation(spec, config.publicGetPath, 'GET')).toBeTruthy();
  const response = await new EventHubApi(request).get(config.publicGetPath);
  expect(response.status(), await response.text()).toBeLessThan(500);
  expect(response.status()).toBeGreaterThanOrEqual(200);
});
