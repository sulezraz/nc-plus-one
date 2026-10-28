# API Design: NC PLUS ONE

This document describes the intended API behaviour; it does not implement the routes.


## USERS

### GET

**Return a list of users**

| Method |   Path    |        Description        | Request Body | Success Code |  Error Codes  |
| :----: | :-------: | :-----------------------: | :----------: | :----------: | :-----------: |
| GET | /users | Return all users | - | 200 OK | - |

TODO check:  If no users exist, return `200 OK` with `{"users": []}`.
Sort by: `username`, `created_at`. Default: `username`, ascending.

**Return a single user by ID**

| Method |      Path      |          Description           | Request Body | Success Code |  Error Codes  |
| :----: | :------------: | :----------------------------: | :----------: | :----------: | :-----------: |
| GET | /users/{id} | Return a single user by ID | - | 200 OK | 404 Not Found  |

TODO add: add proper implementation of errors found in metrotram booking api

### POST

**Creates a new user**

| Method |     Path      |      Description      | Request Body                                                               | Success Code |            Error Codes            |
| :----: | :-----------: | :-------------------: | :------------------------------------------------------------------------- | :----------: | :-------------------------------: |
| POST | /users | Creates a new user | `username` (str), <br>`email` (str), <br>`password` (str) | 201 Created | 409 Conflict, 422 Unprocessable Entity |

An existing email Return `409 Conflict`. Store a password hash in `user_password`; never return the password or its hash.


### PATCH

**Change a user's details**

| Method |      Path      |      Description      |  Request Body   | Success Code |                   Error Codes                    |
| :----: | :------------: | :-------------------: | :-------------: | :----------: | :----------------------------------------------: |
| PATCH | /users/{id} | Update supplied user fields | Any of: `username` (str), `email` (str), `password` (str) | 200 OK | 400 Bad Request, 404 Not Found, 409 Conflict, 422 Unprocessable Entity |


### DELETE

**Delete a user**

| Method |      Path      |   Description    | Request Body | Success Code |                   Error Codes                    |
| :----: | :------------: | :--------------: | :----------: | :----------: | :----------------------------------------------: |
| DELETE | /users/{id} | Delete a user | - | 200 OK | 404 Not Found, 409 Conflict, 422 Unprocessable Entity |



---


## Venues

### GET

**Return a list of venues**

| Method |   Path    |        Description              | Request Body | Success Code |  Error Codes  |
| :----: | :-------: | :-----------------------:       | :----------: | :----------: | :-----------: |
| GET | /venues | Return all venue info | - | 200 OK | 422 Unprocessable Entity |

**Return a single venue by ID**

| Method |   Path    |        Description              | Request Body | Success Code |  Error Codes  |
| :----: | :-------: | :-----------------------:       | :----------: | :----------: | :-----------: |
| GET | /venues/{id} | Return a single venue by ID | - | 200 OK | 404 Not Found, 422 Unprocessable Entity |

**FILTER: Return venues under/over a certain capacity**

| Method |   Path    |        Description              | Request Body | Success Code |  Error Codes  |
| :----: | :-------: | :-----------------------:       | :----------: | :----------: | :-----------: |
| GET | /venues?min_capacity=50&max_capacity=200 | Return venues within the selected capacity range | - | 200 OK | 400 Bad Request, 422 Unprocessable Entity |

Filter by: `min_capacity`, `max_capacity`; either may be omitted. Boundaries are inclusive, and minimum must not exceed maximum. Venues with null capacity do not match capacity filters.

Sort by: `name`, `capacity`. Default: `name`, ascending.


### POST

**Creates a new venue**

| Method |     Path      |      Description      | Request Body                                                               | Success Code |            Error Codes            |
| :----: | :-----------: | :-------------------: | :------------------------------------------------------------------------- | :----------: | :-------------------------------: |
| POST | /venues | Creates a new venue | `name` (str), <br>`address` (str, optional), <br>`capacity` (int, optional) | 201 Created | 422 Unprocessable Entity |


### PATCH

**Change a venue's details**

| Method |      Path      |      Description      |  Request Body   | Success Code |                   Error Codes                    |
| :----: | :------------: | :-------------------: | :-------------: | :----------: | :----------------------------------------------: |
| PATCH | /venues/{id} | Update supplied venue fields | Any of: `name` (str), `address` (str), `capacity` (int) | 200 OK | 400 Bad Request, 404 Not Found, 422 Unprocessable Entity |


### DELETE

**Delete a venue**

| Method |      Path      |   Description    | Request Body | Success Code |                   Error Codes                    |
| :----: | :------------: | :--------------: | :----------: | :----------: | :----------------------------------------------: |
| DELETE | /venues/{id} | Delete a venue | - | 200 OK | 404 Not Found, 409 Conflict, 422 Unprocessable Entity |



---


## Events

### GET

**Return a list of events**

| Method |   Path    |        Description        | Request Body | Success Code |  Error Codes  |
| :----: | :-------: | :-----------------------: | :----------: | :----------: | :-----------: |
| GET | /events | Return all events | - | 200 OK | 422 Unprocessable Entity |

**Return a single event by ID**

| Method |      Path      |          Description           | Request Body | Success Code |  Error Codes  |
| :----: | :------------: | :----------------------------: | :----------: | :----------: | :-----------: |
| GET | /events/{id} | Return a single event by ID | - | 200 OK | 404 Not Found, 422 Unprocessable Entity |

**FILTER: Return events filtered by attendee ID**

| Method |      Path      |          Description           | Request Body | Success Code |  Error Codes  |
| :----: | :------------: | :----------------------------: | :----------: | :----------: | :-----------: |
| GET | /events?attendee_id=3 | Return events filtered by attendee ID | - | 200 OK | 422 Unprocessable Entity |

Requires a join or equivalent query between `events` and `rsvps`. Return each matching event once.

Filter by: `attendee_id`, `organiser_id`, `venue_id`.
Sort by: `starts_at`, `ends_at`, `organiser_id`, `venue_id`. Default: `starts_at`, ascending.


### POST

**Creates a new event**

| Method |     Path      |      Description      | Request Body                                                               | Success Code |            Error Codes            |
| :----: | :-----------: | :-------------------: | :------------------------------------------------------------------------- | :----------: | :-------------------------------: |
| POST | /events | Creates a new event | `title` (str), <br>`description` (str, optional), <br>`starts_at` (datetime), `ends_at` (datetime), `organiser_id` (int, optional), `venue_id` (int, optional) | 201 Created | 400 Bad Request, 404 Not Found, 422 Unprocessable Entity |

Both datetimes are required and must include a timezone, e.g. `"2026-11-15T18:30:00+00:00"`. The end must be after the start; otherwise return `400 Bad Request`. Non-null organiser and venue IDs must reference existing records.


### PATCH

**Change an event's details**

| Method |      Path      |      Description      |  Request Body   | Success Code |                   Error Codes                    |
| :----: | :------------: | :-------------------: | :-------------: | :----------: | :----------------------------------------------: |
| PATCH | /events/{id} | Update supplied event fields | Any of: `title`, `description`, `starts_at`, `ends_at`, `organiser_id`, `venue_id` (same types as POST) | 200 OK | 400 Bad Request, 404 Not Found, 422 Unprocessable Entity |


### DELETE

**Delete an event**

| Method |      Path      |   Description    | Request Body | Success Code |                   Error Codes                    |
| :----: | :------------: | :--------------: | :----------: | :----------: | :----------------------------------------------: |
| DELETE | /events/{id} | Delete an event | - | 200 OK | 404 Not Found, 409 Conflict, 422 Unprocessable Entity |


---


## Event registrations (RSVPs)

### GET

**Return a list of event registrations**

| Method |   Path    |        Description        | Request Body | Success Code |  Error Codes  |
| :----: | :-------: | :-----------------------: | :----------: | :----------: | :-----------: |
| GET | /rsvps | Return all event registrations | - | 200 OK | 422 Unprocessable Entity |

**Return a single event registration by ID**

| Method |      Path      |          Description           | Request Body | Success Code |  Error Codes  |
| :----: | :------------: | :----------------------------: | :----------: | :----------: | :-----------: |
| GET | /rsvps/{id} | Return a single event registration by ID | - | 200 OK | 404 Not Found, 422 Unprocessable Entity |

**FILTER: Return event registrations filtered by attendee ID**

| Method |      Path      |          Description           | Request Body | Success Code |  Error Codes  |
| :----: | :------------: | :----------------------------: | :----------: | :----------: | :-----------: |
| GET | /rsvps?attendee_id=3 | Return event registrations filtered by attendee ID | - | 200 OK | 422 Unprocessable Entity |

Filter by: `attendee_id`, `event_id`.
Sort by: `attendee_id`, `event_id`, `created_at`. Default: `created_at`, ascending.


### POST

**Creates a new event registration**

| Method |     Path      |      Description      | Request Body                                                               | Success Code |            Error Codes            |
| :----: | :-----------: | :-------------------: | :------------------------------------------------------------------------- | :----------: | :-------------------------------: |
| POST | /rsvps | Creates a new event registration | `attendee_id` (int), `event_id` (int) | 201 Created | 404 Not Found, 409 Conflict, 422 Unprocessable Entity |

Both IDs are required and must exist. Registering the same attendee/event pair twice Return `409 Conflict`.


### PATCH

Not needed with the current registration fields. Each RSVP is unique to user. To register for another event, cancel the existing registration and create a new one.


### DELETE

**Cancel an event registration**

| Method |      Path      |   Description    | Request Body | Success Code |                   Error Codes                    |
| :----: | :------------: | :--------------: | :----------: | :----------: | :----------------------------------------------: |
| DELETE | /rsvps/{id} | Cancel an event registration | - | 200 OK | 404 Not Found, 422 Unprocessable Entity |



---



## RESPONSE BODY

**Chosen responses for this design:**

| Method | Action | Typical response body | Success status |
|---|---|---|---|
| **GET** | Retrieve records | A list of records or one record | `200 OK` |
| **POST** | Create a record | The newly created record, including its generated ID | `201 Created` |
| **PATCH** | Update selected fields | The complete updated record | `200 OK` |
| **DELETE** | Remove a record | A deletion confirmation | `200 OK` |

| Resource | List response | Single-record response |
|---|---|---|
| Users | `{"users": [...]}` | `{"user": {...}}` |
| Venues | `{"venues": [...]}` | `{"venue": {...}}` |
| Events | `{"events": [...]}` | `{"event": {...}}` |
| Registrations | `{"rsvps": [...]}` | `{"rsvp": {...}}` |

POST and PATCH return the created or updated record in its single-record wrapper. Records include their generated IDs and public fields; passwords and hashes should be excluded. Examples below abbreviate the returned fields.

For example:

**GET — return existing data**
```json
{
  "user": {
    "user_id": 3,
    "username": "Carol Singh"
  }
}
```

**POST — return the newly created record**
```json
{
  "user": {
    "user_id": 7,
    "username": "New User"
  }
}
```

**PATCH — return the record after updating it**
```json
{
  "user": {
    "user_id": 3,
    "username": "Updated Name"
  }
}
```

**DELETE — return a confirmation with `200`:**
```json
{
  "message": "User deleted"
}
```

**You decide and implement the response structure.** The HTTP method does not automatically determine which data your endpoint Return.

## SHARED RULES

- TODO/TDD - **Empty lists:** all collection GETs, including filters with no matches, return `200 OK` and an empty list. 
  - Use `404` for missing single records or missing related records during POST/PATCH.
- **Validation:** IDs must be positive integers; required text must not be blank. 
  - Check email format, database string-length limits and nonnegative capacity. 
  - Invalid input types/formats return `422 Unprocessable Entity`.
- **PATCH:** accept one or more supplied fields, leaving omitted fields unchanged. 
   - An empty update Return `400`; unknown/read-only fields return `422`. Validate the resulting start/end pair even if only one datetime changes.
- **Generated fields:** IDs and `created_at` are server-controlled and are not accepted in POST/PATCH bodies. 
  - Optional POST fields can be omitted when defined with a default, such as `address: str | None = None`, which defaults to `null`. Without `= None`, the field is required and omitting it causes a **422 validation error**. At database level, omitting a nullable column from an `INSERT` stores `NULL` if no explicit default exists.
- **Filters and sorting:** combine filters using AND. Use `sort_by` and `order=asc` or `order=desc`; default to ascending and break ties using the resource's primary key. Allow only supported sorting fields/directions. Filtered rows above describe the same GET collection route, not separate FastAPI route paths.
- **Deletion:** return `409 Conflict` while users, venues or events still have dependent records. Remove or reassign dependencies first. Deleting a registration keeps the user and event.
- **Authentication:** planned, so blanket `401` entries have been removed. Once implemented, use `401` for missing/invalid authentication and `403` for insufficient permission. IDs alone do not prove who the caller is.

Example combination:

```text
/events?attendee_id=3&sort_by=starts_at&order=asc
```

Application errors use a detail message, e.g. `{"detail": "User not found"}`. FastAPI's automatic `422` validation responses use a list of error details. Endpoint tables list expected client errors, not every possible server failure.

## TODO: API Design Add-Ons
- [ ] Make Filter/Sort APIs for users, events, venues, rsvps

- [ ] Implement and test the routes, response wrappers and error codes.
- [ ] Add combined filters and allowlisted sorting with consistent defaults.
- [ ] Support multiple-field PATCH, omitted fields, nulls and empty-body validation.
- [ ] Enforce unique emails/registrations, valid datetimes/capacity and relationship/deletion rules in the API and database.
- [ ] Add password hashing, authentication and permissions; never return passwords or hashes.
- [ ] Test empty lists, missing records, invalid input, duplicates and relationship conflicts.


### Notes
- **URL parameters do not change SQL automatically.** Adding `sort_by` or `order` to a link only supplies values to the API.
- **The backend must read, validate and apply them.** FastAPI can read declared query parameters, but your database code must choose the corresponding `ORDER BY`.
- **Fixed SQL stays fixed.** `ORDER BY username, user_id` continues sorting by username unless your code uses the supplied sorting choice.
- **Define the supported choices in the API.** For example, users support `username` and `created_at`; events support `starts_at`. Only allow approved fields and `asc`/`desc` directions.
- **One collection route can support multiple combinations.** You do not need a separate route for every filter or sort. Use `?` for the first query parameter and `&` for additional ones.

Example request:
```text
/users?sort_by=created_at&order=desc
```

The backend would select this SQL ordering:
```sql
ORDER BY created_at DESC, user_id ASC;
```

The user ID breaks ties when creation timestamps match.
