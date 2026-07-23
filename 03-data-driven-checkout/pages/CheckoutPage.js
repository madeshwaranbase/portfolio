class CheckoutPage {
  constructor(page) {
    this.page = page;

    // Step one: information form
    this.firstNameInput = page.locator('#first-name');
    this.lastNameInput = page.locator('#last-name');
    this.postalCodeInput = page.locator('#postal-code');
    this.continueButton = page.locator('#continue');
    this.errorMessage = page.locator('[data-test="error"]');

    // Step two: overview
    this.finishButton = page.locator('#finish');
    this.summaryTotalLabel = page.locator('.summary_total_label');

    // Step three: completion
    this.completeHeader = page.locator('.complete-header');
  }

  async fillInformation({ firstName, lastName, postalCode }) {
    await this.firstNameInput.fill(firstName || '');
    await this.lastNameInput.fill(lastName || '');
    await this.postalCodeInput.fill(postalCode || '');
    await this.continueButton.click();
  }

  async getErrorText() {
    return this.errorMessage.textContent();
  }

  async finishOrder() {
    await this.finishButton.click();
  }

  async getCompletionText() {
    return this.completeHeader.textContent();
  }
}

module.exports = { CheckoutPage };
