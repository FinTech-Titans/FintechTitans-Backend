import azure.functions as func
from fastapi import FastAPI
import json

app = FastAPI()

# Sample data - in a real application, this would come from a database
sample_data = {
    "1": {"name": "Item 1", "description": "Description for item 1"},
    "2": {"name": "Item 2", "description": "Description for item 2"},
}

@app.get("/api")
async def read_root():
    return {"message": "Welcome to the Azure Microservice"}

@app.get("/api/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in sample_data:
        return {"error": "Item not found"}, 404
    return sample_data[item_id]

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
