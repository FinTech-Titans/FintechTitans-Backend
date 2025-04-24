from fastapi import APIRouter, HTTPException
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

@router.get("/user-literacy/{user_id}/{topic_id}")
def get_user_literacy(user_id: str, topic_id: str):
    doc_id = f"{user_id}_{topic_id}"
    try:
        item = container.read_item(item=doc_id, partition_key=user_id)
        return item
    except exceptions.CosmosResourceNotFoundError:
        raise HTTPException(status_code=404, detail="User literacy record not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cosmos DB error: {str(e)}")
