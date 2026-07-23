class InventoryPage {
  constructor(page) {
    this.page = page;
    this.cartIcon = page.locator('.shopping_cart_link');
  }

  productAddButton(productName) {
    const slug = productName.toLowerCase().replace(/\s+/g, '-');
    return this.page.locator(`[data-test="add-to-cart-${slug}"]`);
  }

  async addProductToCart(productName) {
    await this.productAddButton(productName).click();
  }

  async goToCart() {
    await this.cartIcon.click();
  }
}

module.exports = { InventoryPage };
