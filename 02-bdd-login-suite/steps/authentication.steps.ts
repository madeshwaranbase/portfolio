import 'dotenv/config';
import { Given, When, Then, After, setDefaultTimeout } from '@cucumber/cucumber';
import { chromium, Browser, Page, expect } from '@playwright/test';

setDefaultTimeout(30_000);
let browser: Browser;
let page: Page;

Given('I open the EventHub login page', async () => {
  browser = await chromium.launch();
  page = await browser.newPage();
  await page.goto(`${process.env.BASE_URL ?? 'https://eventhub.rahulshettyacademy.com'}${process.env.LOGIN_PATH ?? '/login'}`);
});

Then('the email and password fields are visible', async () => {
  await expect(page.locator('input[type="email"]').first()).toBeVisible();
  await expect(page.locator('input[type="password"]').first()).toBeVisible();
});

When('I log in with the configured sandbox account', async () => {
  if (!process.env.EVENTHUB_EMAIL || !process.env.EVENTHUB_PASSWORD) {
    throw new Error('Set EVENTHUB_EMAIL and EVENTHUB_PASSWORD in .env.');
  }
  await page.locator('input[type="email"]').first().fill(process.env.EVENTHUB_EMAIL);
  await page.locator('input[type="password"]').first().fill(process.env.EVENTHUB_PASSWORD);
  await page.locator('form button[type="submit"]').first().click();
});

When('I log in with invalid credentials', async () => {
  await page.locator('input[type="email"]').first().fill('invalid.user@example.com');
  await page.locator('input[type="password"]').first().fill('InvalidPassword!123');
  await page.locator('form button[type="submit"]').first().click();
});

Then('I should see the authenticated navigation', async () => {
  await expect(page.getByTestId('logout-btn')).toBeVisible();
  await expect(page.getByTestId('user-email-display')).toBeVisible();
});

Then('I should not see the authenticated navigation', async () => {
  await expect(page.getByTestId('logout-btn')).toHaveCount(0);
  await expect(page.locator('input[type="password"]').first()).toBeVisible();
});

After(async () => {
  await page?.close();
  await browser?.close();
});
