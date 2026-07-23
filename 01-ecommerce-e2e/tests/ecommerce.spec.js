const { test, expect } = require('../fixtures');
const { credentials, products, address } = require('../utils/testData');

test('Ecommerce end-to-end flow', async ({ loginPage, productsPage, cartPage, checkoutPage, ordersPage }) => {
  await loginPage.goto();
  await loginPage.login(credentials.email, credentials.password);

  await productsPage.goto();
  await productsPage.addProductToCart(products[0]);
  await productsPage.openCart();

  await cartPage.verifyProductInCart(products[0]);
  await cartPage.proceedToCheckout();

  await checkoutPage.selectPaymentType('Credit Card');
  await checkoutPage.fillCreditCardDetails({
    cardNumber: '4542 9931 9292 2293',
    expiryMonth: '01',
    expiryYear: '16',
    cvv: '123',
    nameOnCard: 'Test User',
  });
  await checkoutPage.fillShippingInformation({
    name: credentials.email,
    country: 'India',
  });
  await checkoutPage.placeOrder();

  await ordersPage.goto();
  await ordersPage.verifyOrderExists(products[0]);
});
