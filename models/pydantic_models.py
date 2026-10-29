from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    user_password: str

class UserUpdate(BaseModel):
    username: str
    email: str
    user_password: str

class VenueCreate(BaseModel):
    venue_name: str
    address: str
    capacity: int

class VenueUpdate(BaseModel):
    venue_name: str
    address: str
    capacity: int

class EventCreate(BaseModel):
    event_name: str
    description: str
    starts_at: datetime
    ends_at: datetime
    organiser_id: int
    venue_id: int

class EventUpdate(BaseModel):
    event_name: str
    description: str
    starts_at: datetime
    ends_at: datetime
    organiser_id: int
    venue_id: int

class RsvpCreate(BaseModel):
    attendee_id: int
    event_id: int

class RsvpUpdate(BaseModel):
    attendee_id: int
    event_id: int
