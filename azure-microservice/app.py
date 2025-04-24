from fastapi import FastAPI, HTTPException
from typing import Dict
from routes.user_literacy import router as user_literacy_router
from routes.user import router as user_router
from routes.category import router as category_router
from routes.topic import router as topic_router

app = FastAPI(title="Azure Microservice")



@app.get("/")
def read_root():
    return {"message": "Welcome to the Azure Microservice"}

# Include routers
app.include_router(user_router)
app.include_router(user_literacy_router)
app.include_router(category_router)
app.include_router(topic_router)

