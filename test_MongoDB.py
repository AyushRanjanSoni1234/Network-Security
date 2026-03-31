from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from network_securities.exception import exception
from network_securities.logging.logging import logging
import sys

uri = "mongodb+srv://ars7408984015_db_user:Ayush12345@cluster0.ebhvmfp.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
logging.info("MongoDB client created successfully")

# Send a ping to confirm a successful connection
try:
    logging.info("Pinging MongoDB server to confirm connection")
    client.admin.command('ping')
    logging.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    raise exception.NetworkSecuritiesException(e, sys)
