from network_securities.exception.exception import NetworkSecuritiesException
from network_securities.logging.logging import logging
from network_securities.entity.config_entity import DataIngestionConfig, TraingPipelineConfig
from network_securities.entity.artifact_entity import DataIngestionArtifact

import os
import sys
import pymongo
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from typing import List

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")    

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            logging.info(f"Data Ingestion config: {self.data_ingestion_config}")
        except Exception as e:
            raise NetworkSecuritiesException(e, sys)
    
    def export_collection_as_dataframe(self):
        """
        this function is used to export the data in MongoDB collection as a pandas dataframe.
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.client = pymongo.MongoClient(MONGO_DB_URL)
            logging.info(f"Connected to MongoDB database: {database_name} and collection: {collection_name}")
            collection = self.client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df = df.drop("_id", axis=1)

            df.replace({'na':np.nan}, inplace=True)   
            logging.info(f"Exported collection data as dataframe with shape: {df.shape}")
            return df 

        except Exception as e:
            logging.error(f"Error while exporting collection data as dataframe: {e}")
            raise NetworkSecuritiesException(e, sys)

    def export_data_as_feature_store(self, dataframe: pd.DataFrame):
        """
        This function is used to export the dataframe to feature store as a csv file.
        """
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_dir
            # Create directory if it does not exist
            dir_path = os.path.dirname(feature_store_file_path)
            # os.makedirs(dir_path, exist_ok=True) will create the directory if it does not exist, and do nothing if it already exists
            os.makedirs(dir_path, exist_ok=True)
            # Export the dataframe to feature store as a csv file
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            logging.info(f"Exported data to feature store at path: {feature_store_file_path}")

            return dataframe

        except Exception as e:
            logging.error(f"Error while exporting data to feature store: {e}")
            raise NetworkSecuritiesException(e, sys)    

    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        """
        Splits the dataframe into train and test sets and stores them in the specified file paths.
        """
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=42
                )
            logging.info(f"Performed train test split on the dataframe")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
                )
            logging.info("Training Data is save at path")

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
                )
            logging.info("Testing Data is save at path")

        except Exception as e:
            logging.error(f"Error while splitting data into train and test sets: {e}")
            raise NetworkSecuritiesException(e, sys)    

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_as_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)

            # Create an artifact to return the file paths of the train and test data
            datainmestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )
            logging.info(f"Data Ingestion artifact created")

            return datainmestion_artifact
        except Exception as e:
            raise NetworkSecuritiesException(e, sys)    