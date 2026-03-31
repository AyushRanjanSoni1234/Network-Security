import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(f"MongoDB URL: {MONGO_DB_URL}")

import certifi
ca = certifi.where()

import pymongo
import pandas as pd
import numpy as np
from network_securities.exception.exception import NetworkSecuritiesException
from network_securities.logging.logging import logging

class Network_Data_Extract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecuritiesException(e, sys)
        
    def csv_to_json_converter(self, file_path):
        self.file_path = file_path
        try:
            logging.info(f"Converting CSV file at {file_path} to JSON format")
            df = pd.read_csv(self.file_path)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            logging.info("CSV file successfully converted to JSON format")
            return records
        except Exception as e:
            raise NetworkSecuritiesException(e, sys)    
        
    def insert_data_to_mongodb(self, records, database, collection_name):
        try:
            self.records = records
            self.database = database
            self.collection_name = collection_name

            logging.info(f"Connecting to MongoDB at {MONGO_DB_URL}")
            self.client = pymongo.MongoClient(MONGO_DB_URL)
            logging.info("Successfully connected to MongoDB")

            self.database = self.client[self.database]
            self.collection = self.database[self.collection_name]
            logging.info(f"Inserting records into MongoDB collection: {collection_name}")

            self.collection.insert_many(self.records)
            logging.info("Records successfully inserted into MongoDB")

            return len(self.records)

        except Exception as e:
            raise NetworkSecuritiesException(e, sys)    
        
if __name__ == "__main__":
    file_path = r"D:\Python\Machine Learning\Projects\NetworkSecurity\network_data\phisingData.csv"
    database = "Network_Securities"
    collection_name = "Phishing_Data"

    Network_Data_Extract_obj = Network_Data_Extract()
    records = Network_Data_Extract_obj.csv_to_json_converter(file_path)
    number_of_records = Network_Data_Extract_obj.insert_data_to_mongodb(records, database, collection_name)

    print(f"Number of records inserted into MongoDB: {number_of_records}")