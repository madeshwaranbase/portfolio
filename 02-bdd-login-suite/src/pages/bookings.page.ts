import { expect, Page } from '@playwright/test';
import { config } from '../config/env';

export class BookingsPage {
  constructor(private readonly page: Page) {}
  async open(): Promise<void> {
    await this.page.goto(config.bookingsPath);
    await expect(this.page.getByRole('heading', { name: /my bookings/i })).toBeVisible();
  }
  async assertEmptyState(): Promise<void> {
    await expect(this.page.getByRole('heading', { name: /no bookings yet/i })).toBeVisible();
  }
  async assertBookingVisible(customerEmail: string): Promise<void> {
    await expect(this.page.getByText(customerEmail, { exact: false }).first()).toBeVisible();
  }
}
