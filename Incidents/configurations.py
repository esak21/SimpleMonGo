from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

uri = os.getenv('MONGO_URI')

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.claims

collection  =  db["claims_data"]