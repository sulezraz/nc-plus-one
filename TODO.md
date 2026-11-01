# NC Plus One — Implementation TODO

Build a small database foundation first, then work through **vertical slices**: one selected behaviour, its database work, validation and tests.

Follow this order where work is still needed. Reuse existing code rather than rebuilding it.

## Major tasks
- [x] Set up the project, dependencies and environment configuration.
- [ ] Verify a SQL script can recreate the development database from scratch.
- [x] Create and seed PostgreSQL databases and connect through Psycopg.
- [ ] Establish isolated test data and tests for transformation utilities.
- [ ] Build and test event browsing and event details.
- [ ] Build and test registration, login and authenticated identity.
- [ ] Build and test RSVP creation, cancellation and personal event lists.
- [ ] Build and test organiser event creation and updates.
- [ ] Build and test attendee lists and organiser statistics.
- [ ] Complete the documented validation, permissions and error cases.
- [ ] Verify documentation and portfolio readiness.

The completed major tasks reflect reported progress. Use the detailed checklists to verify individual parts.

## Working method for each slice
1. Choose one observable behaviour.
2. Define its request, response and expected database outcome.
3. Write a focused test.
4. Implement the code needed for that behaviour.
5. Check the response and relevant database effects.
6. Run related tests, tidy the code and commit.
7. Record remaining improvements as later slices.

When using TDD, confirm the test fails because the intended behaviour is missing.

**Do not leave all testing, validation or error handling until the end.** Add them alongside the behaviour they support.

## 1. Prepare the project

**Goal:** Set up the project, dependencies and environment configuration. Use README file.

## 2. Create the databases and connection

**Goal:** connect to separate development and test databases.
- [ ] Start PostgreSQL and create the development database.
- [ ] Store in `db/create_database.sql`.
- [ ] Confirm the script can recreate the disposable development database.
- [ ] Create a separate test database.
- [ ] Configure `.env.development` and `.env.test`.
- [ ] Implement or verify `get_connection()`.
- [ ] Check the actual connected database using `SELECT current_database();`.

Keep database creation separate from table creation and seeding. Destructive setup must not run automatically when the API starts.

## 3. Create tables and seed data

**Goal:** have predictable records available before building database-backed routes.
- [ ] Create `users` and `venues`, then `events`, then `rsvps`.
- [ ] Add primary keys, foreign keys, required-field constraints and unique emails.
- [ ] Use the same schema definitions for development and testing.
- [ ] Load JSON seed records and implement the required transformation helpers.
- [ ] Unit test transformation logic as it is added, including `convert_tuple()`.
- [ ] Insert users and venues before events, then insert RSVPs.
- [ ] Implement the reset-and-seed script.
- [ ] Verify the inserted records and relationships.
- [ ] Handle transactions and release resources on success and failure.

Add further agreed database constraints alongside the features that require them.

**Checkpoint:** a fresh disposable database can be populated predictably. No API router is required yet.

## 4. Establish isolated database test setup

**Goal:** tests can safely use predictable data.
- [ ] Set the test environment and database in `tests/conftest.py` before application or seed imports.
- [ ] Ensure connections are not opened before test settings are selected.
- [ ] Verify the actual database target before destructive test resets.
- [ ] Provide fixtures that reset and seed data when required.
- [ ] Confirm one test’s changes cannot affect another test’s starting state.

Add TestClient with the first API slice below. PostgreSQL must be running for database-backed tests; Uvicorn is not required.

## 5. Build the first endpoint: list events

**Endpoint:** GET `/api/events`

### Slice A — Return seeded events
- [ ] Define the successful status code, response wrapper and public fields.
- [ ] Create the FastAPI application in `main.py`.
- [ ] Create the events router and register its prefix.
- [ ] Add a TestClient fixture for the actual application.
- [ ] Write a test for the expected seeded event response.
- [ ] Implement the query and response conversion.
- [ ] Release database resources on success and failure.
- [ ] Confirm the application also starts with Uvicorn.

### Slice B — Return an empty list
- [ ] Test the endpoint with no event records.
- [ ] Return `200 OK` with an empty collection in the agreed wrapper.

**Move on when:** these behaviours work and their tests pass.

Documented filters and sorting can be added later as separate slices. Each needs validation, query changes and tests.

## 6. Return one event

**Endpoint:** GET `/api/events/{id}`

Reuse the events router and existing test setup.

### Slice A — Return an existing event
- [ ] Test the expected event details.
- [ ] Implement the parameterised lookup and public response.

### Slice B — Handle a missing event
- [ ] Test an event ID that does not exist.
- [ ] Return the documented `404` response.

### Slice C — Validate the ID
- [ ] Test the agreed invalid-ID cases.
- [ ] Add the required validation.

Complete each test-and-implementation cycle before starting the next.

## 7. Register an account

**Endpoint:** POST `/api/auth/register`

Create the auth router and request model when starting this feature.

### Slice A — Create a valid account
- [ ] Test that valid input returns `201` and saves the account.
- [ ] Hash the password before storage.
- [ ] Return only public user fields.
- [ ] Verify persistence through a separate connection or subsequent request.
- [ ] Commit successful changes, roll back failures and release resources.

### Slice B — Reject missing or invalid input
- [ ] Test missing required fields and the validation rules in the current contract.
- [ ] Verify rejected requests create no records.

### Slice C — Reject duplicate emails
- [ ] Test an existing email.
- [ ] Preserve the database uniqueness constraint.
- [ ] Return the documented conflict response.
- [ ] Verify no additional account is created.

Further field rules can be added through later slices. Password hashing belongs in this usable account feature.

## 8. Log in and identify the caller

**Endpoint:** POST `/api/auth/login`

### Slice A — Accept valid credentials
- [ ] Define the authentication response and how later requests supply authentication.
- [ ] Prepare predictable test users with password hashes.
- [ ] Test and implement credential verification and the agreed response.

### Slice B — Reject invalid credentials
- [ ] Test incorrect credentials.
- [ ] Implement the documented rejection response.

### Slice C — Identify authenticated callers
- [ ] Add a reusable way to identify the authenticated caller.
- [ ] Test missing and invalid authentication as protected endpoints are introduced.

A user ID supplied in a URL or body does not prove who made the request.

## 9. Add RSVPs and personal registrations

Seeded events are sufficient for these features. Event creation does not have to be implemented first.

### Slice A — RSVP to an event

**Endpoint:** POST `/api/events/{id}/rsvp`
- [ ] Test and implement an authenticated user registering for an existing event.
- [ ] Test a missing event and missing/invalid authentication.
- [ ] Add a unique user/event constraint.
- [ ] Test duplicate registration rejection.
- [ ] Verify successful persistence and no additional records after rejected requests.

### Slice B — Cancel the caller’s RSVP

**Endpoint:** DELETE `/api/events/{id}/rsvp/me`
- [ ] Test and implement cancellation of the caller’s registration.
- [ ] Verify the user and event records remain.
- [ ] Test the documented missing-event/missing-registration cases.
- [ ] Verify the caller cannot cancel another user’s registration.

### Slice C — View personal events

**Endpoint:** GET `/api/user/me/events`
- [ ] Define whether this includes registered events only or also organised events.
- [ ] Test and implement the agreed event list.
- [ ] Test an empty list.
- [ ] Verify other users’ registrations are excluded.

Finish each slice and its tests before starting the next.

## 10. Create and update organiser events

### Slice A — Create an event

**Endpoint:** POST `/api/events`
- [ ] Define the request fields and how the authenticated organiser is assigned.
- [ ] Test and implement valid creation, persistence and a public response.
- [ ] Test required input, invalid datetimes and missing related records.
- [ ] Enforce the agreed start/end rule in the API and database.
- [ ] Test authentication and any additional creation permissions.

Seeded venues are enough unless venue-management endpoints are required.

### Slice B — Update one event field

**Endpoint:** PATCH `/api/events/{id}`
- [ ] Test and implement an organiser updating one permitted field.
- [ ] Verify omitted fields remain unchanged.
- [ ] Test a missing event and missing authentication.
- [ ] Reject another user’s attempt to edit the event.

### Slice C — Extend the supported updates
- [ ] Support multiple supplied fields.
- [ ] Define and test explicit nulls, empty updates and unknown/read-only fields.
- [ ] Validate the resulting start/end pair when either datetime changes.
- [ ] Verify rejected updates leave the event unchanged.

A complete set of user or venue CRUD endpoints is not automatically required.

## 11. Add attendees and audience statistics

### Slice A — View attendees

**Endpoint:** GET `/api/events/{id}/attendees`
- [ ] Define access permissions and public attendee fields.
- [ ] Test and implement the attendee query and response.
- [ ] Test an empty list, a missing event and access restrictions.

### Slice B — View organiser statistics

**Endpoint:** GET `/api/organisers/{id}/stats`
- [ ] Confirm the required metrics and access policy.
- [ ] Test and implement one metric at a time.
- [ ] Verify results include only the relevant organiser’s events and registrations.
- [ ] Test the agreed no-data, missing-record and permission cases.

Confirm the exact metrics against the course requirements before implementing them.

## 12. Review the complete project

Maintain documentation and commits throughout development. Use this as the final verification pass.
- [ ] Complete every required endpoint’s documented success and error cases.
- [ ] Confirm consistent response wrappers, status codes and error structures.
- [ ] Ensure unexpected failures return generic errors without internal details.
- [ ] Verify password data is excluded from responses.
- [ ] Verify changing request IDs cannot bypass permissions.
- [ ] Run the full test suite with isolated data.
- [ ] Check database resources and failed transactions are handled correctly.
- [ ] Update README setup, seeding, server and test instructions.
- [ ] Document endpoint examples, authentication and feature status.
- [ ] Verify a fresh clone works using only the README.
- [ ] Review Git history and check for committed secrets.

## When to move to the next slice

Move on when:
- [ ] The selected behaviour works through the API.
- [ ] Relevant tests verify meaningful responses and database effects.
- [ ] Existing database integrity rules remain enforced.
- [ ] Resources are released and failed writes leave no unintended changes.
- [ ] Required authentication and permissions are tested.
- [ ] Remaining work is recorded and the change is committed.

**A completed slice is not necessarily a completed endpoint.** Later slices can add validation, filtering, fields or more detailed error handling.

Before marking an endpoint complete for submission, cover all required behaviour and every documented error case.

Refactor repeated code when working examples reveal a useful shared pattern.

Frontend implementation remains outside this project’s scope.