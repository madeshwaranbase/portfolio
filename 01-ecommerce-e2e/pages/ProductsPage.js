class ProductsPage {
  constructor(page) {
    this.page = page;
    this.productCards = page.locator('div.col-lg-4.col-md-6.col-sm-10.offset-md-0.offset-sm-1.mb-3.ng-star-inserted');
    this.addToCartButton = page.locator('button:has-text("Add To Cart")');
    this.cartLink = page.locator('button.btn.btn-custom[routerlink="/dashboard/cart"]');
  }

  async goto() {
    await this.page.goto('https://rahulshettyacademy.com/client/#/dashboard/dash');
    await this.productCards.first().waitFor({ state: 'visible', timeout: 10000 });
  }

  async addProductToCart(productName) {
    const card = this.productCards.filter({ hasText: productName });
    await card.locator(this.addToCartButton).click();
  }

  async openCart() {
    await this.cartLink.click();
    await this.page.waitForURL('**/dashboard/cart', { timeout: 10000 });
  }
}

module.exports = { ProductsPage };
