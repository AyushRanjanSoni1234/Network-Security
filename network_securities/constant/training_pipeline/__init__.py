import os
import sys
import pandas as pd
import numpy as np

"""
Define constants for training pipeline here.
"""
TARGET_COLUMN : str = "Result"
PIPELINE_NAME : str = "Network_Securities_Pipeline"
ARTIFACT_DIR : str = "artifact"
FILE_NAME : str = "phisingData.csv"

TRAIN_FILE_NAME : str = "train.csv"
TEST_FILE_NAME : str = "test.csv"


"""
Data ingestion related constant variable can be defined here.
"""
DATA_INGESTION_COLLECTION_NAME : str = "Phishing_Data"
DATA_INGESTION_DATABASE_NAME : str = "Network_Securities"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2
