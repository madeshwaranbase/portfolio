import { test, expect } from '@playwright/test';
import { config } from '../../src/config/env';
import { LoginPage } from '../../src/pages/login.page';
import { EventsPage } from '../../src/pages/events.page';

test.describe('Event discovery', () => {
  test.beforeEach(async ({ page }) => {
    test.skip(!config.hasCredentials, 'Configure EventHub sandbox credentials.');
    const login = new LoginPage(page);
    await login.open();
    await login.signInWithConfiguredUser();
  });

  test('upcoming events are displayed', async ({ page }) => {
    const events = new EventsPage(page);
    await events.open();
    await expect(events.cards.first()).toBeVisible();
    await expect(page.getByTestId('nav-events')).toBeVisible();
  });

  test('search filters by event name', async ({ page }) => {
    const events = new EventsPage(page);
    await events.open();
    await events.searchFor('Dilli Diwali Mela');
    await expect(events.cards.filter({ hasText: 'Dilli Diwali Mela' })).toBeVisible();
  });

  test('category and city filters accept documented option values', async ({ page }) => {
    const events = new EventsPage(page);
    await events.open();
    await events.filterByCategory('Festival');
    await expect(events.category).toHaveValue('Festival');
    await events.filterByCity('Delhi');
    await expect(events.city).toHaveValue('Delhi');
  });

  test('search with unmatched text produces no matching event card', async ({ page }) => {
    const events = new EventsPage(page);
    await events.open();
    await events.searchFor(`no-event-${Date.now()}`);
    await expect(events.cards).toHaveCount(0);
  });
});
