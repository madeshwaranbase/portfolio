import { test, expect } from '@playwright/test';
import { LoginPage } from '../../src/pages/login.page';
import { config } from '../../src/config/env';

test('login screen presents email, password and submit controls', async ({ page }) => {
  const login = new LoginPage(page);
  await login.open();
  await expect(login.email).toBeVisible();
  await expect(login.password).toBeVisible();
  await expect(login.submit).toBeVisible();
});

test('valid sandbox account can authenticate and logout', async ({ page }) => {
  test.skip(!config.hasCredentials, 'Configure EventHub sandbox credentials.');
  const login = new LoginPage(page);
  await login.open();
  await login.signInWithConfiguredUser();
  await login.logout();
});

test('invalid credentials do not establish an authenticated session', async ({ page }) => {
  const login = new LoginPage(page);
  await login.open();
  await login.signIn('invalid.user@example.com', 'InvalidPassword!123');
  await expect(login.email).toBeVisible();
  await expect(page.getByTestId('logout-btn')).toHaveCount(0);
});
