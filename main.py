from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.logging.logger import logging
import sys

if __name__== "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")
        data_ingestion_artifact = data_ingestion.initate_data_ingetsion()
        data_validation_config = DataValidationConfig(training_pipeline_config)
        logging.info("Data Initiation Completed")
        print(data_ingestion_artifact)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)    