import os
from azure.cosmos import CosmosClient

COSMOS_ENDPOINT = os.environ.get("COSMOS_ENDPOINT", "https://fintechtitanscosmos.documents.azure.com:443/")
COSMOS_KEY = os.environ.get("COSMOS_KEY", "<secret_key>")  # Replace with your key or use env var
COSMOS_DB = "FintechTitansDB"
COSMOS_CONTAINER = "UserLiteracy"

cosmos_client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = cosmos_client.get_database_client(COSMOS_DB)
container = database.get_container_client(COSMOS_CONTAINER)
