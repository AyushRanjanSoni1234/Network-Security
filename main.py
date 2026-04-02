from network_securities.exception.exception import NetworkSecuritiesException
from network_securities.logging.logging import logging
from network_securities.components.data_ingestion import DataIngestion
from network_securities.entity.config_entity import DataIngestionConfig, TraingPipelineConfig, DataValidationConfig
import sys
import os
from network_securities.components.data_validation import DataValidation


if __name__ == "__main__":
    try:
        logging.info("Starting data ingestion process")
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=TraingPipelineConfig())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)

        datainmestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion process completed successfully")

        logging.info("Starting data validation process")
        data_validation_config = DataValidationConfig(training_pipeline_config=TraingPipelineConfig())
        data_validation = DataValidation(data_ingestion_artifact=datainmestion_artifact, data_validation_config=data_validation_config) 
        
        data_validation.initiate_data_validation()
        logging.info("Data validation process completed successfully")
        
    except Exception as e:
        logging.error(f"Error occurred while initiating data ingestion: {e}")
        raise NetworkSecuritiesException(e, sys)
