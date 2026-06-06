const { expect } = require('@playwright/test');

class CheckoutPage {
  constructor(page) {
    this.page = page;
    this.paymentSection = page.locator('.payment');
    this.paymentTypeButtons = page.locator('.payment__type');
    this.cardNumberInput = page.locator('.payment__cc .field:has-text("Credit Card Number") input');
    this.expiryMonthSelect = page.locator('.payment__cc select.input.ddl').first();
    this.expiryYearSelect = page.locator('.payment__cc select.input.ddl').nth(1);
    this.cvvInput = page.locator('.payment__cc .field:has-text("CVV Code") input');
    this.nameOnCardInput = page.locator('.payment__cc .field:has-text("Name on Card") input');
    this.couponInput = page.locator('input[name="coupon"]');
    this.applyCouponButton = page.locator('button:has-text("Apply Coupon")');
    this.shippingNameInput = page.locator('.payment__shipping .details__user input[type="text"]').first();
    this.countryInput = page.locator('.payment__shipping .form-group input[placeholder="Select Country"]');
    this.placeOrderButton = page.locator('.btnn.action__submit');
  }

  async goto() {
    await this.page.goto('/dashboard/checkout');
    await expect(this.paymentSection).toBeVisible();
  }

  async selectPaymentType(type) {
    await this.paymentTypeButtons.filter({ hasText: type }).click();
  }

  async fillCreditCardDetails({ cardNumber, expiryMonth, expiryYear, cvv, nameOnCard }) {
    await this.cardNumberInput.fill(cardNumber);
    await this.expiryMonthSelect.selectOption({ label: expiryMonth });
    await this.expiryYearSelect.selectOption({ label: expiryYear });
    await this.cvvInput.fill(cvv);
    await this.nameOnCardInput.fill(nameOnCard);
  }

  async applyCoupon(code) {
    await this.couponInput.fill(code);
    await this.applyCouponButton.click();
  }

  async fillShippingInformation({ name, country }) {
    await this.shippingNameInput.fill(name);
    await this.countryInput.fill(country);
  }

  async placeOrder() {
    await this.placeOrderButton.click();
  }
}

module.exports = { CheckoutPage };
