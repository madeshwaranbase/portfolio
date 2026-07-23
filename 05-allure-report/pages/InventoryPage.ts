import { Page, Locator, expect } from '@playwright/test';
import { allure } from 'allure-playwright';

export class InventoryPage {
  private readonly page: Page;
  private readonly cartBadge: Locator;
  private readonly cartIcon: Locator;
  private readonly sortDropdown: Locator;
  private readonly itemPrices: Locator;

  constructor(page: Page) {
    this.page = page;
    this.cartBadge = page.locator('.shopping_cart_badge');
    this.cartIcon = page.locator('.shopping_cart_link');
    this.sortDropdown = page.locator('[data-test="product-sort-container"]');
    this.itemPrices = page.locator('.inventory_item_price');
  }

  private addButton(productName: string): Locator {
    const slug = productName.toLowerCase().replace(/\s+/g, '-');
    return this.page.locator(`[data-test="add-to-cart-${slug}"]`);
  }

  async addToCart(productName: string) {
    await allure.step(`Add "${productName}" to cart`, async () => {
      await this.addButton(productName).click();
    });
  }

  async expectCartCount(count: number) {
    await allure.step(`Verify cart badge shows ${count}`, async () => {
      await expect(this.cartBadge).toHaveText(String(count));
    });
  }

  async sortBy(option: 'lohi' | 'hilo' | 'az' | 'za') {
    await allure.step(`Sort products by "${option}"`, async () => {
      await this.sortDropdown.selectOption(option);
    });
  }

  async getPrices(): Promise<number[]> {
    return allure.step('Read displayed prices', async () => {
      const texts = await this.itemPrices.allTextContents();
      return texts.map((t) => parseFloat(t.replace('$', '')));
    });
  }
}
