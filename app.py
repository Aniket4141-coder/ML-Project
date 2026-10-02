import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    logging.info("Execution of Data Ingestion Pipeline started")
    
    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        print(f"Train dataset saved at: {train_data_path}")
        print(f"Test dataset saved at: {test_data_path}")

    except Exception as e:
        logging.info("Custom Exception occurred")
        raise CustomException(e, sys)