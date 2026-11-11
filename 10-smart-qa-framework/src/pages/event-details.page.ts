import { expect, Locator, Page } from '@playwright/test';

export class EventDetailsPage {
  readonly name: Locator;
  readonly email: Locator;
  readonly phone: Locator;
  readonly ticketCount: Locator;
  readonly increment: Locator;
  readonly decrement: Locator;
  readonly confirm: Locator;
  readonly total: Locator;

  constructor(private readonly page: Page) {
    this.name = page.locator('#customerName');
    this.email = page.getByTestId('customer-email');
    this.phone = page.locator('#phone');
    this.ticketCount = page.locator('#ticket-count');
    const form = page.locator('form').filter({ has: page.locator('#confirm-booking') });
    this.increment = form.getByRole('button', { name: '+' });
    this.decrement = form.getByRole('button', { name: '−' });
    this.confirm = page.locator('#confirm-booking');
    this.total = form.locator('div').filter({ hasText: /^Total/ }).last();
  }

  async assertLoaded(): Promise<void> {
    await expect(this.page.getByRole('heading', { name: /book tickets/i })).toBeVisible();
    await expect(this.name).toBeVisible();
    await expect(this.email).toBeVisible();
    await expect(this.phone).toBeVisible();
    await expect(this.confirm).toBeVisible();
  }

  async assertRequiredFields(): Promise<void> {
    await expect(this.name).toHaveAttribute('required', '');
    await expect(this.email).toHaveAttribute('required', '');
    await expect(this.phone).toHaveAttribute('required', '');
  }

  async setCustomer(name: string, email: string, phone: string): Promise<void> {
    await this.name.fill(name);
    await this.email.fill(email);
    await this.phone.fill(phone);
  }

  async setTicketQuantity(quantity: number): Promise<void> {
    if (!Number.isInteger(quantity) || quantity < 1 || quantity > 10) {
      throw new Error('Ticket quantity must be an integer between 1 and 10.');
    }
    let current = Number((await this.ticketCount.innerText()).trim());
    while (current < quantity) { await this.increment.click(); current += 1; }
    while (current > quantity) { await this.decrement.click(); current -= 1; }
    await expect(this.ticketCount).toHaveText(String(quantity));
  }

  async submit(): Promise<void> {
    await this.confirm.click();
  }

  async assertBookingOutcome(customerEmail: string): Promise<void> {
    // The app's success banner text is not assumed. Verify a real post-submit state:
    // either a confirmation message is visible or the new booking is present in My Bookings.
    const successMessage = this.page.getByText(/booking (confirmed|successful|created)|successfully booked/i).first();
    const confirmationRoute = /\/(bookings|booking)(?:\/|$|\?)/i;
    await expect.poll(async () => {
      const routeChanged = confirmationRoute.test(new URL(this.page.url()).pathname);
      const messageVisible = await successMessage.isVisible().catch(() => false);
      return routeChanged || messageVisible;
    }, { timeout: 15_000 }).toBeTruthy();

    if (!confirmationRoute.test(new URL(this.page.url()).pathname)) {
      await this.page.goto('/bookings');
    }
    await expect(this.page.getByRole('heading', { name: /my bookings/i })).toBeVisible();
    await expect(this.page.getByText(customerEmail, { exact: false }).first()).toBeVisible();
  }
}
