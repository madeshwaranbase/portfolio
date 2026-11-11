# Architecture Decision Record

## Design
- Playwright Test is the execution engine.
- Page objects encapsulate UI interaction.
- Fixtures establish authenticated browser state per test.
- API clients use APIRequestContext and configurable OpenAPI-derived operations.
- Mutating workflows are explicitly opt-in.
- CI retains HTML reports, traces and failure artifacts.

## Trade-offs
The EventHub API route definitions are not embedded because the live Swagger JSON was not readable in the documentation retrieval environment. The framework requires the real contract as configuration rather than encoding guesses.
