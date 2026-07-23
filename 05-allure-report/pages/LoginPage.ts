import { Page, Locator, expect } from '@playwright/test';
import { allure } from 'allure-playwright';

export class LoginPage {
  private readonly page: Page;
  private readonly usernameInput: Locator;
  private readonly passwordInput: Locator;
  private readonly loginButton: Locator;
  private readonly errorMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.usernameInput = page.locator('#user-name');
    this.passwordInput = page.locator('#password');
    this.loginButton = page.locator('#login-button');
    this.errorMessage = page.locator('[data-test="error"]');
  }

  async goto() {
    await allure.step('Navigate to login page', async () => {
      await this.page.goto('/');
    });
  }

  async login(username: string, password: string) {
    await allure.step(`Log in as "${username}"`, async () => {
      await this.usernameInput.fill(username);
      await this.passwordInput.fill(password);
      await this.loginButton.click();
    });
  }

  async expectLoginError(expectedText: string) {
    await allure.step('Verify login error message is shown', async () => {
      await expect(this.errorMessage).toContainText(expectedText);
    });
  }

  async expectLoggedIn() {
    await allure.step('Verify redirected to inventory page', async () => {
      await expect(this.page).toHaveURL(/inventory.html/);
    });
  }
}
