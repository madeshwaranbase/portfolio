const { expect } = require('@playwright/test');

class OrdersPage {
  constructor(page) {
    this.page = page;
    this.orderTable = page.locator('table.table-bordered.table-hover');
    this.orderRows = this.orderTable.locator('tbody tr');
  }

  async goto() {
    await this.page.goto('https://rahulshettyacademy.com/client/#/dashboard/myorders');
    await expect(this.orderTable).toBeVisible();
  }

  async verifyOrderExists(productName) {
    const matchingRows = this.orderRows.filter({ hasText: productName });
    await expect(matchingRows).toHaveCount(1);
  }

  async getOrderIdForProduct(productName) {
    const matchingRow = this.orderRows.filter({ hasText: productName }).first();
    return matchingRow.locator('th[scope="row"]').innerText();
  }

  async viewOrder(productName) {
    const matchingRow = this.orderRows.filter({ hasText: productName }).first();
    await matchingRow.locator('button:has-text("View")').click();
  }

  async deleteOrder(productName) {
    const matchingRow = this.orderRows.filter({ hasText: productName }).first();
    await matchingRow.locator('button:has-text("Delete")').click();
    await expect(matchingRow).not.toBeVisible();
  }
}

module.exports = { OrdersPage };
