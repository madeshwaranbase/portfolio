import { test as base, expect, Page } from '@playwright/test';
import { config } from '../config/env';
import { LoginPage } from '../pages/login.page';

type Fixtures = { authenticatedPage: Page };

export const test = base.extend<Fixtures>({
  authenticatedPage: async ({ page }, use) => {
    if (!config.hasCredentials) throw new Error('Set EVENTHUB_EMAIL and EVENTHUB_PASSWORD in .env.');
    const login = new LoginPage(page);
    await login.open();
    await login.signInWithConfiguredUser();
    await use(page);
  }
});
export { expect };
