import { test, expect } from '@playwright/test';
import { config, parseJsonEnv } from '../../src/config/env';
import { loadOpenApi, hasOperation, jsonPath } from '../../src/api/eventhub-api';

test('API login token can authorize a documented protected GET operation', async ({ request }) => {
  test.skip(
    !config.openApiSpecUrl || !config.apiLoginPath || !config.apiLoginPayload || !config.publicGetPath,
    'Configure the actual OpenAPI JSON URL, login operation/payload and protected GET path from Swagger.'
  );

  const spec = await loadOpenApi(request);
  expect(hasOperation(spec, config.apiLoginPath, config.apiLoginMethod)).toBeTruthy();
  expect(hasOperation(spec, config.publicGetPath, 'GET')).toBeTruthy();

  const payload = parseJsonEnv<Record<string, unknown>>('API_LOGIN_PAYLOAD_JSON', config.apiLoginPayload);
  const loginResponse = await request.fetch(
    `${config.apiBaseUrl}/${config.apiLoginPath.replace(/^\/+/, '')}`,
    {
      method: config.apiLoginMethod,
      data: payload,
      headers: { Accept: 'application/json', 'Content-Type': 'application/json' }
    }
  );
  expect(loginResponse.status(), await loginResponse.text()).toBeLessThan(300);

  const loginBody = await loginResponse.json();
  const token = jsonPath(loginBody, config.apiTokenJsonPath);
  expect(token, `Token not found at configured JSON path ${config.apiTokenJsonPath}`).toBeTruthy();

  const protectedResponse = await request.get(
    `${config.apiBaseUrl}/${config.publicGetPath.replace(/^\/+/, '')}`,
    { headers: { Accept: 'application/json', Authorization: `Bearer ${String(token)}` } }
  );
  expect(protectedResponse.status(), await protectedResponse.text()).toBeLessThan(500);
});
