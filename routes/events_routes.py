# events_routes.py
# Defines events endpoints, such as GET /events/, and the functions that handle their requests.

from fastapi import APIRouter, HTTPException

from db.connection import get_connection

events_router = APIRouter(prefix="/events")


# -- GET -- # 

# -- Return a list of events
#       Order by event_name ASC -- #
@events_router.get("/")
def get_all_events():
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
def get_events_member(event_id: int):
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


