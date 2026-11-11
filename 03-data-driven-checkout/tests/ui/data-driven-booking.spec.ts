import { test, expect } from '@playwright/test';
import cases from '../../test-data/booking-cases.json';
import { config } from '../../src/config/env';
import { LoginPage } from '../../src/pages/login.page';
import { EventsPage } from '../../src/pages/events.page';

test.describe('Data-driven booking field validation', () => {
  test.beforeEach(async ({ page }) => {
    test.skip(!config.hasCredentials, 'Configure EventHub sandbox credentials.');
    const login = new LoginPage(page);
    await login.open();
    await login.signInWithConfiguredUser();
    const events = new EventsPage(page);
    await events.open();
    await events.openEventByName('Dilli Diwali Mela');
  });

  for (const row of cases) {
    test(`case ${row.caseId}`, async ({ page }) => {
      await page.locator('#customerName').fill(row.name);
      const email = page.getByTestId('customer-email');
      await email.fill(row.email);
      await page.locator('#phone').fill(row.phone);
      await expect(email).toHaveJSProperty('validity.valid', row.expectedEmailValid);
      // Do not submit data-driven validation cases; they must remain non-mutating.
    });
  }
});
