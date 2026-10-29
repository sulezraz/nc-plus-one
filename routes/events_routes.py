# events_routes.py
# Defines events endpoints, such as GET /events/, and the functions that handle their requests.
import sys
from datetime import datetime

sys.path.insert(0,"/home/suleyman/projects/northcoders/2projects/nc-plus-one")

from fastapi import APIRouter, HTTPException
from rich.pretty import pprint

from db.connection import get_connection
from models.pydantic_models import EventsCreate, EventsUpdate

events_router = APIRouter(prefix="/events")

#-----------#
# -- GET -- # 
#-----------#

# -- Return a list of events
#       Order by event_name ASC -- #
@events_router.get("/")
def get_all_events() -> dict[str, list[dict]]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""--sql
        SELECT *
        FROM events
        ORDER BY event_name, event_id;
    """)

    assert cur.description is not None
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()

    cur.close()
    conn.close()

    if not rows:
        print("TERRIFYING: No events have been found.")

    # Map database columns to row values; an empty result returns [].
    events = [dict(zip(columns, row)) for row in rows]
    return {"events": events}


# -- Returns a single event by ID -- #
@events_router.get("/{event_id}")
def get_event(event_id: int) -> dict[str, dict]:
    
    conn = get_connection()
    cur = conn.cursor()

    query = """--sql
        SELECT *
        FROM events
        WHERE event_id = %s;  -- Keep only rows where event_id = the supplied parameter value.
    """

    # Pass values separately so the driver handles SQL parameters safely.
    cur.execute(query, (event_id,))

    assert cur.description is not None
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Event not found. Did you check the bin.")

    event = dict(zip(columns, row))
    return {"event": event}



#------------#
# -- POST -- # 
#------------#

# -- Add a new event -- #
@events_router.post("/", status_code=201) # Return HTTP 201 Created when the route completes successfully.
def create_event(event: EventsCreate) -> dict[str, dict]:
    
    conn = get_connection()
    cur = conn.cursor()
    
    query = """--sql
        INSERT INTO events (
            event_name,
            description,
            starts_at,
            ends_at,
            organiser_id,
            venue_id
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING *;
    """

    # Pass values separately so the driver handles SQL parameters safely.
    cur.execute(
        query,
        (
            event.event_name,
            event.description,
            event.starts_at,
            event.ends_at,
            event.organiser_id,
            event.venue_id,
        ),
    )
    
    assert cur.description is not None          # CHECK: sql query must return column metadata
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()

    conn.commit()  # Save the transaction's changes.
    cur.close()   # Release the cursor
    conn.close()  # Close the connection
    
    if row is None:
        raise RuntimeError("Event insert did not return the expected row.")

    posted_event = dict(zip(columns, row))
    return {"event": posted_event}







# # -- MANUAL RESPONSE INSPECTION -- #
# if __name__ == "__main__":
#     pprint("ALL EVENTS:")
#     pprint(get_all_events())
#     print()

#     pprint("SINGLE EVENT:")
#     pprint(get_event(1))  # Use a event ID that exists.


# -- MANUAL RESPONSE INSPECTION -- #
if __name__ == "__main__":
    new_event = EventsCreate(
        event_name="Python Workshop",
        description="An introduction to Python.",
        starts_at="2026-01-05T12:34:00", # type: ignore
        ends_at="2026-02-15T10:45:00", # type: ignore
        organiser_id=1,
        venue_id=1,
    )

    pprint("CREATED EVENT:")
    pprint(create_event(new_event))
