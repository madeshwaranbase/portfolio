import { test } from '@playwright/test';
import { allure } from 'allure-playwright';
import { LoginPage } from '../pages/LoginPage';

test.describe('Login', () => {
  test.beforeEach(async () => {
    await allure.epic('Authentication');
    await allure.feature('Login');
  });

  test('standard_user logs in successfully', async ({ page }) => {
    await allure.severity('critical');
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login('standard_user', 'secret_sauce');
    await loginPage.expectLoggedIn();
  });

  test('locked_out_user is blocked with an error', async ({ page }) => {
    await allure.severity('critical');
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login('locked_out_user', 'secret_sauce');
    await loginPage.expectLoginError('Sorry, this user has been locked out');
  });

  test('wrong password shows generic error', async ({ page }) => {
    await allure.severity('normal');
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login('standard_user', 'wrong_password');
    await loginPage.expectLoginError('Username and password do not match');
  });
});
