import { expect, Locator, Page } from '@playwright/test';
import { config } from '../config/env';

export class EventsPage {
  readonly cards: Locator;
  readonly search: Locator;
  readonly category: Locator;
  readonly city: Locator;

  constructor(private readonly page: Page) {
    this.cards = page.getByTestId('event-card');
    this.search = page.getByPlaceholder(/search events, venues/i);
    this.category = page.locator('main select').nth(0);
    this.city = page.locator('main select').nth(1);
  }

  async open(): Promise<void> {
    await this.page.goto(config.eventsPath);
    await expect(this.page.getByRole('heading', { name: /upcoming events/i })).toBeVisible();
  }

  async searchFor(term: string): Promise<void> {
    await this.search.fill(term);
  }

  async filterByCategory(value: string): Promise<void> {
    await this.category.selectOption(value);
  }

  async filterByCity(value: string): Promise<void> {
    await this.city.selectOption(value);
  }

  async openEventByName(name: string): Promise<void> {
    const card = this.cards.filter({ hasText: name }).first();
    await expect(card, `Event card "${name}" should be visible`).toBeVisible();
    await card.getByTestId('book-now-btn').click();
  }

  async openFirstAvailableEvent(): Promise<void> {
    const card = this.cards.first();
    await expect(card).toBeVisible();
    await card.getByTestId('book-now-btn').click();
  }
}
