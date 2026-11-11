import { test, expect } from '@playwright/test';
import { config } from '../../src/config/env';
import { LoginPage } from '../../src/pages/login.page';
import { EventsPage } from '../../src/pages/events.page';
import { EventDetailsPage } from '../../src/pages/event-details.page';

test.describe('Event booking form', () => {
  test.beforeEach(async ({ page }) => {
    test.skip(!config.hasCredentials, 'Configure EventHub sandbox credentials.');
    const login = new LoginPage(page);
    await login.open();
    await login.signInWithConfiguredUser();
    const events = new EventsPage(page);
    await events.open();
    await events.openEventByName('Dilli Diwali Mela');
  });

  test('booking form exposes required customer fields', async ({ page }) => {
    const details = new EventDetailsPage(page);
    await details.assertLoaded();
    await details.assertRequiredFields();
  });

  test('ticket quantity can be increased and decreased within limits', async ({ page }) => {
    const details = new EventDetailsPage(page);
    await details.assertLoaded();
    await details.setTicketQuantity(3);
    await details.setTicketQuantity(1);
  });

  test('email input rejects malformed email using browser validity', async ({ page }) => {
    const details = new EventDetailsPage(page);
    await details.email.fill('not-an-email');
    await expect(details.email).toHaveJSProperty('validity.valid', false);
  });

  test('booking form is not submitted by validation-only scenarios', async ({ page }) => {
    const details = new EventDetailsPage(page);
    await details.assertLoaded();
    await expect(details.confirm).toBeEnabled();
    // Intentionally no submit: this test is non-mutating.
  });
});
