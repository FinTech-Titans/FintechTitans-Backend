from fastapi import FastAPI, HTTPException
from typing import Dict
from routes.user_literacy import router as user_literacy_router

app = FastAPI(title="Azure Microservice")

# Sample data - in a real application, this would come from a database
sample_data = {
    "1": {"name": "Item 1", "description": "Description for item 1"},
    "2": {"name": "Item 2", "description": "Description for item 2"},
}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Azure Microservice"}

@app.get("/items/{item_id}")
def read_item(item_id: str) -> Dict:
    if item_id not in sample_data:
        raise HTTPException(status_code=404, detail="Item not found")
    return sample_data[item_id]

# Include user literacy router
app.include_router(user_literacy_router)

