import { test, expect } from '@playwright/test';

test('EventHub public home page visual baseline', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('heading', { name: /discover & book/i })).toBeVisible();
  await expect(page).toHaveScreenshot('eventhub-home.png', {
    fullPage: true, animations: 'disabled', caret: 'hide'
  });
});

test('EventHub login screen visual baseline', async ({ page }) => {
  await page.goto('/login');
  await expect(page.locator('input[type="email"]').first()).toBeVisible();
  await expect(page).toHaveScreenshot('eventhub-login.png', {
    fullPage: true, animations: 'disabled', caret: 'hide'
  });
});
