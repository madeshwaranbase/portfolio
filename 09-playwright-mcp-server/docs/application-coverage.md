# EventHub Application Coverage

Grounded UI selectors captured from the supplied EventHub page HTML:
- Navigation: `nav-home`, `nav-events`, `nav-bookings`
- Authenticated user: `user-email-display`, `logout-btn`
- Event list: `event-card`, `book-now-btn`
- Event search placeholder: `Search events, venues…`
- Event filters: first and second `main select` (category and city)
- Booking form: `#ticket-count`, `#customerName`, `#customer-email`, `#phone`, `#confirm-booking`
- Empty booking state: heading `No bookings yet`

Known routes observed in the supplied page captures: `/`, `/events`, `/bookings`, and event detail routes such as `/events/285`.

Login form selectors are implemented using semantic input types/placeholders because a login page HTML capture was not included. Verify the actual login form if the app changes.
