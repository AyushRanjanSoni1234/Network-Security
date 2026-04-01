from network_securities.exception.exception import NetworkSecuritiesException
from network_securities.logging.logging import logging
from network_securities.components.data_ingestion import DataIngestion
from network_securities.entity.config_entity import DataIngestionConfig, TraingPipelineConfig
from network_securities.entity.artifact_entity import DataIngestionArtifact
import sys
import os


if __name__ == "__main__":
    try:
        logging.info("Starting data ingestion process")
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=TraingPipelineConfig())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)

        datainmestion_artifact = data_ingestion.initiate_data_ingestion()
        print(datainmestion_artifact)
        logging.info("Data ingestion process completed successfully")
        
    except Exception as e:
        logging.error(f"Error occurred while initiating data ingestion: {e}")
        raise NetworkSecuritiesException(e, sys)
