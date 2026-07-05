import { Given, When, Then } from '@cucumber/cucumber';
import { expect } from '@playwright/test';

Given('The user is on the login page', async function () {
  await this.page.goto('https://eventhub.rahulshettyacademy.com/login');
});

When('The user enters the username {string}', async function (username: string) {
  await this.page.getByPlaceholder('you@email.com').fill(username);
});

When('The user enters the password {string}', async function (password: string) {
  await this.page.getByPlaceholder('••••••').fill(password);
});

When('The user clicks on the login button', async function () {
  await this.page.locator('#login-btn').click();
});

Then('The user should be redirected to the dashboard page', async function () {
  await this.page.waitForURL('https://eventhub.rahulshettyacademy.com/');
});