import 'dotenv/config';

function required(name: string, fallback?: string): string {
  const value = (process.env[name] ?? fallback ?? '').trim();
  if (!value) throw new Error(`Missing required environment variable: ${name}`);
  return value;
}

export const config = {
  baseUrl: process.env.BASE_URL ?? 'https://eventhub.rahulshettyacademy.com',
  loginPath: process.env.LOGIN_PATH ?? '/login',
  eventsPath: process.env.EVENTS_PATH ?? '/events',
  bookingsPath: process.env.BOOKINGS_PATH ?? '/bookings',
  apiBaseUrl: (process.env.API_BASE_URL ?? 'https://api.eventhub.rahulshettyacademy.com').replace(/\/$/, ''),
  openApiSpecUrl: process.env.OPENAPI_SPEC_URL?.trim() ?? '',
  email: process.env.EVENTHUB_EMAIL?.trim() ?? '',
  password: process.env.EVENTHUB_PASSWORD ?? '',
  apiToken: process.env.API_TOKEN?.trim() ?? '',
  publicGetPath: process.env.API_PUBLIC_GET_PATH?.trim() ?? '',
  apiLoginPath: process.env.API_LOGIN_PATH?.trim() ?? '',
  apiLoginMethod: (process.env.API_LOGIN_METHOD ?? 'POST').toUpperCase(),
  apiLoginPayload: process.env.API_LOGIN_PAYLOAD_JSON ?? '',
  apiTokenJsonPath: process.env.API_TOKEN_JSON_PATH ?? 'access_token',
  apiBookingPath: process.env.API_BOOKING_PATH?.trim() ?? '',
  apiBookingMethod: (process.env.API_BOOKING_METHOD ?? 'POST').toUpperCase(),
  apiBookingPayload: process.env.API_BOOKING_PAYLOAD_JSON ?? '',
  runMutatingTests: (process.env.RUN_MUTATING_TESTS ?? 'false').toLowerCase() === 'true',
  get hasCredentials() { return Boolean(this.email && this.password); }
};

export function parseJsonEnv<T>(name: string, raw: string): T {
  try { return JSON.parse(raw) as T; }
  catch { throw new Error(`${name} must be valid JSON. Check quoting and escaping in .env.`); }
}
