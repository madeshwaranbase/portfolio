const { expect } = require('@playwright/test');

class CartPage {
  constructor(page) {
    this.page = page;
    this.cartContainer = page.locator('ul.cartWrap');
    this.cartItems = this.cartContainer.locator('li.items');
    this.checkoutButton = page.locator('.subtotal button:has-text("Checkout")');
    this.continueShoppingButton = page.locator('button:has-text("Continue Shopping")');
    this.subtotalValue = page.locator('.subtotal .totalRow .value').first();
    this.totalValue = page.locator('.subtotal .totalRow .value').nth(1);
  }

  async goto() {
    await this.page.goto('/dashboard/cart');
    await expect(this.cartContainer).toBeVisible();
  }

  async verifyProductInCart(productName) {
    const matchingItem = this.cartItems.filter({ hasText: productName });
    await expect(matchingItem).toHaveCount(1);
  }

  async removeProduct(productName) {
    const matchingItem = this.cartItems.filter({ hasText: productName }).first();
    await matchingItem.locator('button.btn-danger').click();
  }

  async buyNow(productName) {
    const matchingItem = this.cartItems.filter({ hasText: productName }).first();
    await matchingItem.locator('button:has-text("Buy Now")').click();
  }

  async proceedToCheckout() {
    await this.checkoutButton.click();
  }

  async getSubtotal() {
    return this.subtotalValue.innerText();
  }

  async getTotal() {
    return this.totalValue.innerText();
  }
}

module.exports = { CartPage };
