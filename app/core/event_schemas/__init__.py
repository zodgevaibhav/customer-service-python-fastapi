from pydantic import BaseModel
from api.model import User

class UserCreatedEvent(BaseModel):
    user: User

class UserDeletedEvent(BaseModel):
    user_id: int 