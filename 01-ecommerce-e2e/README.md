# 🛒 E-Commerce E2E Test Suite — Playwright

A portfolio project showcasing end-to-end test automation skills using **Playwright** with a **Page Object Model (POM)** architecture, built with **JavaScript**.

**Target Application:** [rahulshettyacademy.com/client](https://rahulshettyacademy.com/client)

---

## 📌 Project Overview

This project demonstrates real-world QA automation practices including structured test design, reusable page objects, custom fixtures, and centralized test data management — all applied to a live e-commerce web application.

---

## ✅ Test Coverage

| Flow | Description |
|------|-------------|
| 🔐 Login | Valid user authentication |
| 🛍️ Browse Products | Search and select products from the catalogue |
| 🛒 Add to Cart | Add multiple products and verify cart state |
| 💳 Checkout | Fill shipping details and place order |
| 📦 Order History | Verify placed order appears in order history |

---

## 🏗️ Project Structure

```
ecommerce-pw/
├── fixtures/
│   └── index.js              # Custom test fixtures — injects page objects into tests
├── pages/
│   ├── LoginPage.js          # Login page selectors and actions
│   ├── ProductsPage.js       # Product listing, search, add to cart
│   ├── CartPage.js           # Cart view and proceed to checkout
│   ├── CheckoutPage.js       # Address form and order placement
│   └── OrdersPage.js         # Order history verification
├── tests/
│   └── ecommerce.spec.js     # Main E2E test spec
├── utils/
│   └── testData.js           # Centralized test credentials and product data
├── playwright.config.js
└── package.json
```

---

## 🧱 Architecture Highlights

- **Page Object Model (POM)** — each page is a class with its own selectors and action methods
- **Custom Fixtures** — page objects are injected via `test.extend()` for clean, DRY test code
- **Centralized Test Data** — credentials and product names managed in `utils/testData.js`
- **Playwright Config** — base URL, browser settings, and timeouts configured in `playwright.config.js`

---

## 🚀 Getting Started

### Prerequisites
- Node.js v18+
- npm

### Installation

```bash
git clone https://github.com/madeshwaranbase/portfolio.git
cd portfolio
npm install
npx playwright install
```

### Run Tests

```bash
# Run all tests
npx playwright test

# Run with UI mode
npx playwright test --ui

# Run headed (see browser)
npx playwright test --headed

# View HTML report
npx playwright show-report
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Playwright](https://playwright.dev) | Browser automation framework |
| JavaScript (ES6+) | Test scripting language |
| Page Object Model | Test architecture pattern |
| HTML Reporter | Built-in Playwright test reporting |

---

## 👨‍💻 Author

**Madeshwaran Ponnudurai**  
QA Automation Engineer  
[GitHub](https://github.com/madeshwaranbase)

---

> Built to demonstrate end-to-end automation skills with industry-standard patterns.
