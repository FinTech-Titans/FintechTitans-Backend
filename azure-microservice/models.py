from pydantic import BaseModel

class LiteracyUpdateRequest(BaseModel):
    userId: str
    topicId: str
    literacyPercentage: int
