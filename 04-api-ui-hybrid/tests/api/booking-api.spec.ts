import { test, expect } from '@playwright/test';
import { config, parseJsonEnv } from '../../src/config/env';
import { loadOpenApi, hasOperation } from '../../src/api/eventhub-api';

test('configured booking API operation accepts the contract-shaped payload', async ({ request }) => {
  test.skip(
    !config.runMutatingTests || !config.openApiSpecUrl || !config.apiBookingPath || !config.apiBookingPayload,
    'This test creates a booking. Set RUN_MUTATING_TESTS=true and configure the exact booking operation and payload from Swagger.'
  );

  const spec = await loadOpenApi(request);
  expect(hasOperation(spec, config.apiBookingPath, config.apiBookingMethod)).toBeTruthy();
  const payload = parseJsonEnv<Record<string, unknown>>('API_BOOKING_PAYLOAD_JSON', config.apiBookingPayload);
  const response = await request.fetch(
    `${config.apiBaseUrl}/${config.apiBookingPath.replace(/^\/+/, '')}`,
    {
      method: config.apiBookingMethod,
      data: payload,
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        ...(config.apiToken ? { Authorization: `Bearer ${config.apiToken}` } : {})
      }
    }
  );
  expect(response.status(), await response.text()).toBeGreaterThanOrEqual(200);
  expect(response.status(), await response.text()).toBeLessThan(300);
});
