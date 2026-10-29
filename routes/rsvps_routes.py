# rsvps_routes.py
# Defines rsvps endpoints, such as GET /rsvps/, and the functions that handle their requests.

from fastapi import APIRouter, HTTPException

from db.connection import get_connection
from models.pydantic_models import RsvpCreate, RsvpUpdate

rsvps_router = APIRouter(prefix="/rsvps")


# -- GET -- # 

# -- Return a list of event registrations
#       Order by created_at ASC -- #
@rsvps_router.get("/")
def get_all_rsvps() -> dict[str, list[dict]]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""--sql
        SELECT *
        FROM rsvps
        ORDER BY created_at, rsvp_id;
    """)

    assert cur.description is not None
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()

    cur.close()
    conn.close()

    if not rows:
        print("TERRIFYING: No rsvps have been found.")

    # Map database columns to row values; an empty result returns [].
    rsvps = [dict(zip(columns, row)) for row in rows]
    return {"rsvps": rsvps}


# -- Returns a single rsvp by ID -- #
@rsvps_router.get("/{rsvp_id}")
def get_rsvps(rsvp_id: int) -> dict[str, dict]:
    conn = get_connection()
    cur = conn.cursor()

    query = """--sql
        SELECT *
        FROM rsvps
        WHERE rsvp_id = %s;  -- Keep only rows where rsvp_id = the supplied parameter value.
    """

    # Pass values separately so the driver handles SQL parameters safely.
    cur.execute(query, (rsvp_id,))

    assert cur.description is not None
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="rsvp not found. Did you check the bin.")

    rsvp = dict(zip(columns, row))
    return {"rsvp": rsvp}


#------------#
# -- POST -- # 
#------------#

# -- Add a new rsvp -- #
@rsvps_router.post("/", status_code=201) # Return HTTP 201 Created when the route completes successfully.
def create_rsvp(rsvp: RsvpCreate) -> dict[str, dict]:
    
    conn = get_connection()
    cur = conn.cursor()
    
    query = """--sql
        INSERT INTO rsvps (
            attendee_id,
            event_id
        )
        VALUES (%s, %s)
        RETURNING *;
    """

    # Pass values separately so the driver handles SQL parameters safely.
    cur.execute(
        query,
        (
            rsvp.attendee_id,
            rsvp.event_id,
        ),
    )
    
    assert cur.description is not None          # CHECK: sql query must return column metadata
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()

    conn.commit()  # Save the transaction's changes.
    cur.close()   # Release the cursor
    conn.close()  # Close the connection
    
    assert row is not None
    
    posted_rsvp = dict(zip(columns, row))
    return {"rsvp": posted_rsvp}





# # -- MANUAL RESPONSE INSPECTION -- #
# if __name__ == "__main__":
#     pprint("ALL RSVPs:")
#     pprint(get_all_rsvps())
#     print()

#     pprint("SINGLE RSVP:")
#     pprint(get_rsvp(1))  # Use a rsvp ID that exists.