from fastapi import APIRouter, HTTPException
from azure.cosmos import CosmosClient, exceptions
from db import COSMOS_ENDPOINT, COSMOS_KEY, COSMOS_DB
from typing import List

# Cosmos DB Topics container setup
client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.get_database_client(COSMOS_DB)
topics_container = database.get_container_client("Topics")

router = APIRouter()

@router.get("/categories/{category_id}/topics", response_model=List[dict])
def get_topics_for_category(category_id: str):
    try:
        query = "SELECT * FROM c WHERE c.categoryId = @categoryId"
        params = [{"name": "@categoryId", "value": category_id}]
        topics = list(topics_container.query_items(
            query=query,
            parameters=params,
            enable_cross_partition_query=True
        ))
        return topics
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cosmos DB error: {str(e)}")

@router.get("/topics/{topic_id}")
def get_topic(topic_id: str):
    try:
        topic = topics_container.read_item(item=topic_id, partition_key=topic_id)
        return topic
    except exceptions.CosmosResourceNotFoundError:
        raise HTTPException(status_code=404, detail="Topic not found in Cosmos DB")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cosmos DB error: {str(e)}")
