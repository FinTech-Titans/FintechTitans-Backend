from fastapi import APIRouter, HTTPException
from azure.cosmos import exceptions
from models import LiteracyUpdateRequest
from db import container

router = APIRouter()

@router.post("/user-literacy/update")
def update_user_literacy(data: LiteracyUpdateRequest):
    doc_id = f"{data.userId}_{data.topicId}"
    item = {
        "id": doc_id,
        "userId": data.userId,
        "topicId": data.topicId,
        "literacyPercentage": data.literacyPercentage,
        "_partitionKey": data.userId
    }
    try:
        container.upsert_item(item)
        return {"message": "User literacy updated in Cosmos DB.", "data": item}
    except exceptions.CosmosHttpResponseError as e:
        raise HTTPException(status_code=500, detail=f"Cosmos DB error: {str(e)}")
