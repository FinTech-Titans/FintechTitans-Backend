from fastapi import APIRouter, HTTPException
from azure.cosmos import exceptions
from db import CosmosClient, COSMOS_ENDPOINT, COSMOS_KEY, COSMOS_DB
from models import UserCreateRequest
from typing import Dict

# Cosmos DB Users container setup
users_client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = users_client.get_database_client(COSMOS_DB)
users_container = database.get_container_client("Users")

router = APIRouter()

@router.get("/users/{user_id}")
def read_user(user_id: str) -> Dict:
    try:
        user = users_container.read_item(item=user_id, partition_key=user_id)
        # Return only the required fields
        filtered = {
            "id": user.get("id"),
            "displayName": user.get("displayName"),
            "email": user.get("email")
        }
        return filtered
    except exceptions.CosmosResourceNotFoundError:
        raise HTTPException(status_code=404, detail="User not found in Cosmos DB")

@router.post("/users/create")
def create_user(user: UserCreateRequest):
    user_doc = user.dict()
    user_doc["_partitionKey"] = user.id
    try:
        users_container.read_item(item=user.id, partition_key=user.id)
        raise HTTPException(status_code=409, detail="User already exists")
    except exceptions.CosmosResourceNotFoundError:
        users_container.create_item(body=user_doc)
        return {"message": "User created successfully.", "data": user_doc}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cosmos DB error: {str(e)}")
