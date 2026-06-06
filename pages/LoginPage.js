class LoginPage {
  constructor(page) {
    this.page = page;
    this.emailInput = page.locator('#userEmail');
    this.passwordInput = page.locator('#userPassword');
    this.loginButton = page.locator('#login');
  }

  async goto() {
    await this.page.goto('https://rahulshettyacademy.com/client/#/auth/login');
    await this.emailInput.waitFor({ state: 'visible', timeout: 10000 });
  }

  async login(email, password) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }
}

module.exports = { LoginPage };
