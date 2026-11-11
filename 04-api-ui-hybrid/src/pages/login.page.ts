import { expect, Locator, Page } from '@playwright/test';
import { config } from '../config/env';

export class LoginPage {
  readonly email: Locator;
  readonly password: Locator;
  readonly submit: Locator;

  constructor(private readonly page: Page) {
    this.email = page.locator('input[type="email"]').first()
      .or(page.getByPlaceholder(/email/i).first());
    this.password = page.locator('input[type="password"]').first()
      .or(page.getByPlaceholder(/password/i).first());
    this.submit = page.locator('form button[type="submit"]').first()
      .or(page.getByRole('button', { name: /login|log in|sign in/i }).first());
  }

  async open(): Promise<void> {
    await this.page.goto(config.loginPath);
    await expect(this.email).toBeVisible();
    await expect(this.password).toBeVisible();
    await expect(this.submit).toBeVisible();
  }

  async signIn(email: string, password: string): Promise<void> {
    await this.email.fill(email);
    await this.password.fill(password);
    await this.submit.click();
  }

  async signInWithConfiguredUser(): Promise<void> {
    if (!config.hasCredentials) throw new Error('Set EVENTHUB_EMAIL and EVENTHUB_PASSWORD in .env.');
    await this.signIn(config.email, config.password);
    await this.assertAuthenticated();
  }

  async assertAuthenticated(): Promise<void> {
    await expect(this.page.getByTestId('logout-btn')).toBeVisible();
    await expect(this.page.getByTestId('user-email-display')).toBeVisible();
  }

  async logout(): Promise<void> {
    await this.page.getByTestId('logout-btn').click();
    await expect(this.email).toBeVisible();
  }
}
