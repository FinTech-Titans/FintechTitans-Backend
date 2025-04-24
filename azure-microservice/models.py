from pydantic import BaseModel
from typing import Optional

class LiteracyUpdateRequest(BaseModel):
    userId: str
    topicId: str
    literacyPercentage: int

class UserCreateRequest(BaseModel):
    id: str  # userId, also used as partition key
    displayName: str
    email: str
    sharingAllowed: Optional[bool] = True
    createdAt: Optional[str] = None  # ISO string, optional
