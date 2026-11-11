import { test, expect } from '@playwright/test';
import { config } from '../../src/config/env';
import { loadOpenApi, listOperations } from '../../src/api/eventhub-api';

test('OpenAPI quality gate verifies a non-empty documented API surface', async ({ request }) => {
  test.skip(!config.openApiSpecUrl, 'Configure OPENAPI_SPEC_URL.');
  const spec = await loadOpenApi(request);
  const operations = listOperations(spec);
  expect(operations.length).toBeGreaterThan(0);
  for (const item of operations) {
    expect(item.path.startsWith('/')).toBeTruthy();
  }
});
