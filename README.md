# EventHub Enterprise SDET Portfolio — 10 Independent Projects

This delivery contains ten separately installable project folders and ten individual ZIP archives.

The project concepts are intentionally distinct:
1. E2E customer journey
2. BDD authentication
3. Data-driven booking validation
4. API/UI hybrid and API token chaining
5. Allure reporting
6. Visual regression
7. Python failure analyzer
8. Python OpenAPI test design generator
9. Restricted Playwright MCP server
10. Integrated smart QA framework

## Important validation boundary
The provided EventHub page captures were used to ground observed UI selectors and routes. The live web retrieval of the API Swagger page exposed only its title and no readable endpoint definitions. Therefore, API paths and payloads are loaded/configured from the actual OpenAPI JSON at runtime; no endpoint paths or payload schemas have been invented. The projects have not been executed against your private account in this environment.

## Security
No account password is included. Put your own credentials into each project's local `.env`. Do not commit it. Booking creation is disabled unless explicitly enabled.
