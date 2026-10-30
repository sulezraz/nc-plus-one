"""Define pydantic input models for creating and updating  users, venues, events, and RSVPs."""
from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    """Data required to create a user."""
    username: str
    email: str
    password: str


class UserUpdate(BaseModel):
    """Data required to update a user."""

    username: str
    email: str
    password: str


class VenueCreate(BaseModel):
    """Data required to create a venue."""
    venue_name: str
    address: str
    capacity: int


class VenueUpdate(BaseModel):
    """Data required to update a venue."""
    venue_name: str
    address: str
    capacity: int


class EventCreate(BaseModel):
    """Data required to create an event."""
    event_name: str
    description: str
    starts_at: datetime
    ends_at: datetime
    organiser_id: int
    venue_id: int


class EventUpdate(BaseModel):
    """Data required to update an event."""
    event_name: str
    description: str
    starts_at: datetime
    ends_at: datetime
    organiser_id: int
    venue_id: int


class RsvpCreate(BaseModel):
    """Data required to create an RSVP."""
    attendee_id: int
    event_id: int


class RsvpUpdate(BaseModel):
    """Data required to update an RSVP."""
    attendee_id: int
    event_id: int