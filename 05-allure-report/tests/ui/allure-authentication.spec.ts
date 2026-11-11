import { test, expect } from '@playwright/test';
import { allure } from 'allure-playwright';

test('EventHub login page exposes credential controls', async ({ page }) => {
  await allure.epic('EventHub');
  await allure.feature('Authentication');
  await allure.story('Login page');
  await allure.severity('critical');
  await allure.step('Navigate to login', async () => {
    await page.goto(`${process.env.BASE_URL ?? 'https://eventhub.rahulshettyacademy.com'}${process.env.LOGIN_PATH ?? '/login'}`);
  });
  await allure.step('Verify credential controls', async () => {
    await expect(page.locator('input[type="email"]').first()).toBeVisible();
    await expect(page.locator('input[type="password"]').first()).toBeVisible();
  });
  await allure.attachment('Current page URL', page.url(), 'text/plain');
});
