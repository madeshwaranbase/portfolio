import { test } from '@playwright/test';
import { config } from '../../src/config/env';
import { LoginPage } from '../../src/pages/login.page';
import { EventsPage } from '../../src/pages/events.page';
import { EventDetailsPage } from '../../src/pages/event-details.page';
import { BookingsPage } from '../../src/pages/bookings.page';

test('customer can create a booking and find it in My Bookings', async ({ page }) => {
  test.skip(!config.runMutatingTests, 'Set RUN_MUTATING_TESTS=true to create a real practice booking.');
  test.skip(!config.hasCredentials, 'Configure EventHub sandbox credentials.');

  const login = new LoginPage(page);
  await login.open();
  await login.signInWithConfiguredUser();

  const events = new EventsPage(page);
  await events.open();
  await events.openEventByName('Dilli Diwali Mela');

  const booking = new EventDetailsPage(page);
  await booking.assertLoaded();

  const uniqueEmail = `qa.eventhub.${Date.now()}@example.com`;
  const uniqueName = `QA Automation ${Date.now()}`;
  await booking.setTicketQuantity(2);
  await booking.setCustomer(uniqueName, uniqueEmail, '+919876543210');
  await booking.submit();
  await booking.assertBookingOutcome(uniqueEmail);

  const bookings = new BookingsPage(page);
  await bookings.open();
  await bookings.assertBookingVisible(uniqueEmail);
});
