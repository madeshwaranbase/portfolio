import { Page, Locator, expect } from '@playwright/test';

export class LoginPage {
  private readonly page: Page;
  private readonly emailInput: Locator;
  private readonly passwordInput: Locator;
  private readonly loginButton: Locator;
  private readonly loggedInAsLabel: Locator;
  private readonly loginErrorText: Locator;

  constructor(page: Page) {
    this.page = page;
    this.emailInput = page.locator('input[data-qa="login-email"]');
    this.passwordInput = page.locator('input[data-qa="login-password"]');
    this.loginButton = page.locator('button[data-qa="login-button"]');
    this.loggedInAsLabel = page.locator('a:has-text("Logged in as")');
    this.loginErrorText = page.locator('p:has-text("incorrect")');
  }

  async goto() {
    await this.page.goto('https://automationexercise.com/login');
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async expectLoggedInAs(name: string) {
    await expect(this.loggedInAsLabel).toContainText(name);
  }

  async expectInvalidLoginError() {
    await expect(this.loginErrorText).toBeVisible();
  }
}
