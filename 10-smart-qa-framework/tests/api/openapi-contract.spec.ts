import { test, expect } from '@playwright/test';
import { loadOpenApi, listOperations } from '../../src/api/eventhub-api';

test('EventHub publishes a valid OpenAPI document and operations', async ({ request }) => {
  test.skip(!process.env.OPENAPI_SPEC_URL, 'Configure the exact OpenAPI JSON URL from Swagger.');
  const spec = await loadOpenApi(request);
  const operations = listOperations(spec);
  expect(operations.length).toBeGreaterThan(0);
  console.log(`Contract: ${spec.info?.title ?? 'EventHub API'} ${spec.info?.version ?? ''}`);
  console.log(`Documented operations: ${operations.length}`);
});
