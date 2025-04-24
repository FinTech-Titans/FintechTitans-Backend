# Azure Microservice

A simple microservice built with FastAPI for deployment on Azure.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
uvicorn app:app --reload
```

3. Access the API:
- Main endpoint: http://localhost:8000
- Get item by ID: http://localhost:8000/items/{item_id}

## API Endpoints

- GET `/`: Welcome message
- GET `/items/{item_id}`: Get item details by ID
