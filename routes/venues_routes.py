# venues_routes.py
# Defines venues endpoints, such as GET /venues/, and the functions that handle their requests.

from fastapi import APIRouter, HTTPException
from rich.pretty import pprint

from db.connection import get_connection

venues_router = APIRouter(prefix="/venues")

#-----------#
# -- GET -- # 
#-----------#

# -- Return a list of venues
#       Order by venue id ASC -- #
@venues_router.get("/")
def get_all_venues() -> dict[str, list[dict]]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""--sql
        SELECT *
        FROM venues
        ORDER BY venue_id, venue_name;
    """)

    assert cur.description is not None     # checks that column metadata is available
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()           # fetchall() returns [] when no rows match.

    cur.close()
    conn.close()

    if not rows:
        print("TERRIFYING: No venues have been found.")

    venues = [dict(zip(columns, row)) for row in rows]
    return {"venues": venues}



# TODO: **FILTER: Return venues under/over a certain capacity**. 
# Filter by: `min_capacity`, `max_capacity`; either may be omitted. 
# Boundaries are inclusive, and minimum must not exceed maximum. 
# Venues with null capacity do not match capacity filters.


# -- Returns a single venue by ID -- #
@venues_router.get("/{venue_id}")
def get_venue(venue_id: int) -> dict[str, dict]:
    conn = get_connection()
    cur = conn.cursor()
    
    query = """--sql
        SELECT *
        FROM venues
        WHERE venue_id = %s;  -- Keep only rows where venue_id = the supplied parameter value.
    """

    # Pass values separately so the driver handles SQL parameters safely.
    cur.execute(query, (venue_id,))
    
    assert cur.description is not None
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()
    
    cur.close()
    conn.close()

    if not row:     # if nothing is returned from SQL query then raise Exception
        raise HTTPException(status_code=404, detail="Venue not found. That's worrying.")

    venue = dict(zip(columns, row))
    return {"venue": venue}







# # -- MANUAL RESPONSE INSPECTION -- #
# if __name__ == "__main__":
#     pprint("ALL VENUES:")
#     pprint(get_all_venues())
#     print()

#     pprint("SINGLE VENUE:")
#     pprint(get_venue(1))  # Use a venue ID that exists.