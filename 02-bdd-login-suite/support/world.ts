import { setWorldConstructor, World } from '@cucumber/cucumber';
import { Page } from '@playwright/test';

class CustomWorld extends World {
  page!: Page;
}

setWorldConstructor(CustomWorld);