from fastapi import APIRouter, HTTPException
from azure.cosmos import CosmosClient, exceptions
from db import COSMOS_ENDPOINT, COSMOS_KEY, COSMOS_DB
from typing import List

# Cosmos DB Categories container setup
categories_client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = categories_client.get_database_client(COSMOS_DB)
categories_container = database.get_container_client("Categories")

router = APIRouter()

@router.get("/categories", response_model=List[dict])
def get_all_categories():
    try:
        categories = list(categories_container.read_all_items())
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cosmos DB error: {str(e)}")

@router.get("/categories/{category_id}")
def get_category(category_id: str):
    try:
        category = categories_container.read_item(item=category_id, partition_key=category_id)
        return category
    except exceptions.CosmosResourceNotFoundError:
        raise HTTPException(status_code=404, detail="Category not found in Cosmos DB")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cosmos DB error: {str(e)}")
