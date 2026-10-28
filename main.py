# main.py
# Creates the FastAPI application and registers the users routes.

# Start the development server from the project root:
# python -m uvicorn main:app --reload

from fastapi import FastAPI
from routes.rsvps_routes import rsvps_router

from routes.events_routes import events_router
from routes.users_routes import users_router
from routes.venues_routes import venues_router

# Create the application.
app = FastAPI()

# Register the users endpoints with the application.
app.include_router(users_router)
app.include_router(venues_router)
app.include_router(events_router)
app.include_router(rsvps_router)
