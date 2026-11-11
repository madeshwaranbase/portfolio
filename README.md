# Madeshwaran P | Playwright Portfolio

A collection of 10 independent projects demonstrating automation framework development, UI and API testing, test architecture, reporting, and AI-assisted quality engineering.

Each project is maintained as a separate repository with its own source code, dependencies, configuration, documentation, and execution instructions.

## Projects

### 01. E-Commerce E2E Automation
**Focus:** End-to-end UI automation

- Automates customer workflows from login to booking.
- Uses Playwright and TypeScript.
- Implements Page Object Model and reusable fixtures.
- Covers positive and negative scenarios.

**Repository:** `ecommerce-e2e-automation`

### 02. BDD Authentication Suite
**Focus:** Behaviour-Driven Development

- Implements readable Gherkin scenarios.
- Uses Cucumber-based BDD workflows.
- Separates feature files, step definitions and page objects.
- Covers authentication scenarios.

**Repository:** `bdd-authentication-suite`

### 03. Data-Driven Testing Framework
**Focus:** Parameterization and test coverage

- Executes tests using multiple datasets.
- Covers positive, negative and boundary scenarios.
- Separates test data from automation logic.
- Improves test maintainability.

**Repository:** `data-driven-booking-tests`

### 04. API + UI Hybrid Framework
**Focus:** API automation and integration testing

- Combines API and browser automation.
- Demonstrates authentication and token chaining.
- Supports API-driven test setup.
- Validates workflows across application layers.

**Repository:** `api-ui-hybrid-framework`

### 05. Allure Reporting Framework
**Focus:** Test reporting and observability

- Integrates Allure reporting.
- Organizes execution results and test evidence.
- Supports failure investigation.
- Improves test execution visibility.

**Repository:** `allure-reporting-framework`

### 06. Visual Regression Testing
**Focus:** UI consistency and screenshot comparison

- Captures and compares UI screenshots.
- Detects visual differences.
- Supports baseline-based validation.
- Helps identify unintended UI changes.

**Repository:** `visual-regression-testing`

### 07. Python Test Failure Analyzer
**Focus:** Automated failure analysis

- Processes test execution results.
- Analyzes failure messages and stack traces.
- Groups and summarizes test failures.
- Demonstrates Python-based QA utilities.

**Repository:** `python-test-failure-analyzer`

### 08. OpenAPI Test Generator
**Focus:** API test design automation

- Reads OpenAPI specifications.
- Identifies API operations and request information.
- Generates test design suggestions.
- Demonstrates Python-based API testing utilities.

**Repository:** `openapi-test-generator`

### 09. Playwright MCP Server
**Focus:** Browser automation tooling

- Demonstrates a Playwright-based MCP server.
- Exposes controlled browser automation capabilities.
- Supports structured tool interactions.
- Applies restrictions to permitted browser operations.

**Repository:** `playwright-mcp-server`

### 10. Smart QA Automation Framework
**Focus:** Integrated quality engineering

- Combines UI and API automation capabilities.
- Uses reusable framework components.
- Supports configurable test execution.
- Demonstrates integrated QA workflows.

**Repository:** `smart-qa-automation-framework`

## Technology Stack

| Area | Technologies |
|---|---|
| Programming | Python, TypeScript, JavaScript |
| UI Automation | Playwright, Selenium WebDriver |
| Test Frameworks | PyTest, Playwright Test, Cucumber |
| API Testing | Postman, Python Requests, Playwright API |
| Design Patterns | Page Object Model, Fixtures |
| Reporting | Allure, HTML Reports |
| CI/CD | GitHub Actions, Jenkins |
| AI-Assisted QA | Python, LLM integrations |
| Version Control | Git, GitHub |

## Engineering Practices

- Modular and reusable automation architecture.
- Page Object Model implementation.
- Environment-based configuration.
- Data-driven and parameterized testing.
- Positive, negative and boundary test scenarios.
- API authentication and integration workflows.
- Cross-browser testing.
- Reporting and failure diagnostics.
- CI/CD integration.
- Secure credential management.

## Application Under Test

Some projects use the EventHub practice application as their test environment:

- **Web application:** https://eventhub.rahulshettyacademy.com/login
- **API documentation:** https://api.eventhub.rahulshettyacademy.com/api/docs/

The application is a shared practice target. It is not a parent repository or dependency between the ten projects.

## Repository Independence

Every project is designed to have its own:

- README and technical documentation.
- Source code and test cases.
- Dependency management.
- Environment configuration.
- Execution commands.
- GitHub repository and version history.

Refer to the individual repository README for setup, configuration and execution instructions.

## Validation Notes

The projects demonstrate automation framework implementations and engineering patterns. Live execution, application-specific selector verification, API contract validation and CI pipeline execution must be completed in the target environment before treating the projects as production-validated.

Credentials and tokens must be supplied locally through environment variables. Never commit `.env` files or sensitive test data.

## About Me

I am an Automation Test Engineer focused on building maintainable automation frameworks and improving software quality through UI automation, API testing and intelligent testing solutions.

**Technical Focus:** Python · Selenium · Playwright · TypeScript · PyTest · API Automation · CI/CD

**GitHub:** [madeshwaranbase](https://github.com/madeshwaranbase)
