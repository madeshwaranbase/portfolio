import { Given, When, Then } from '@cucumber/cucumber';
import { expect } from '@playwright/test';
import { CustomWorld } from '../support/world';
import { buildRandomUser } from '../api/userFactory';
import { AccountApiClient } from '../api/accountApiClient';
import { LoginPage } from '../pages/LoginPage';

const apiClient = new AccountApiClient();

Given('I have a randomly generated user account payload', function (this: CustomWorld) {
  this.user = buildRandomUser();
});

Given('the account has already been created via the API', async function (this: CustomWorld) {
  const responseCode = await apiClient.createAccount(this.user);
  expect(responseCode).toBe(201);
});

When('I create the account using the API', async function (this: CustomWorld) {
  this.apiResponseCode = await apiClient.createAccount(this.user);
});

Then('the API should confirm the account was created', function (this: CustomWorld) {
  expect(this.apiResponseCode).toBe(201);
});

When('I open the login page', async function (this: CustomWorld) {
  const loginPage = new LoginPage(this.page);
  await loginPage.goto();
});

When("I log in with the created account's credentials", async function (this: CustomWorld) {
  const loginPage = new LoginPage(this.page);
  await loginPage.login(this.user.email, this.user.password);
});

Then("the UI should show me logged in as the created account's name", async function (this: CustomWorld) {
  const loginPage = new LoginPage(this.page);
  await loginPage.expectLoggedInAs(this.user.firstname);
});

Then('the UI should show an invalid login error', async function (this: CustomWorld) {
  const loginPage = new LoginPage(this.page);
  await loginPage.expectInvalidLoginError();
});

When('I delete the account using the API', async function (this: CustomWorld) {
  this.apiResponseCode = await apiClient.deleteAccount(this.user.email, this.user.password);
  expect(this.apiResponseCode).toBe(200);
});
