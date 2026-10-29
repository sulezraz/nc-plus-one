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
    

class EventsCreate(BaseModel):
    event_name: str
    description: str
    starts_at: datetime
    ends_at: datetime
    organiser_id: int
    venue_id: int

class EventsUpdate(BaseModel):
    event_name: str
    description: str
    starts_at: datetime
    ends_at: datetime
    organiser_id: int
    venue_id: int
    
    
    
    