const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');
const { InventoryPage } = require('../pages/InventoryPage');
const { CartPage } = require('../pages/CartPage');
const { CheckoutPage } = require('../pages/CheckoutPage');
const { loadData } = require('../utils/testDataReader');

const checkoutData = loadData('checkoutData.json');

test.describe('Data-driven checkout flow', () => {
  for (const data of checkoutData) {
    test(`checkout - ${data.scenario}`, async ({ page }) => {
      const loginPage = new LoginPage(page);
      const inventoryPage = new InventoryPage(page);
      const cartPage = new CartPage(page);
      const checkoutPage = new CheckoutPage(page);

      await loginPage.goto();
      await loginPage.login(data.username, data.password);
      await expect(page).toHaveURL(/inventory.html/);

      await inventoryPage.addProductToCart(data.product);
      await inventoryPage.goToCart();
      await cartPage.proceedToCheckout();

      await checkoutPage.fillInformation({
        firstName: data.firstName,
        lastName: data.lastName,
        postalCode: data.postalCode,
      });

      if (data.expected === 'known_broken') {
        // problem_user's checkout "Continue" click is intentionally broken
        // on saucedemo.com — it stays on step-one instead of advancing.
        await expect(page).toHaveURL(/checkout-step-one.html/);
      } else if (data.expected === 'success') {
        await expect(page).toHaveURL(/checkout-step-two.html/);
        await checkoutPage.finishOrder();
        await expect(page).toHaveURL(/checkout-complete.html/);
        await expect(checkoutPage.completeHeader).toHaveText('Thank you for your order!');
      } else {
        const errorText = await checkoutPage.getErrorText();
        expect(errorText).toContain('Error');
      }
    });
  }
});