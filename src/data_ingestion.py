import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.custom_exception import CustomException
from src.logger import get_logger
from config.paths_config import *
from utils.common_functions import read_yaml

logger=get_logger(__name__)
class DatIngestion:
    def __init__(self,config):
        self.config=config["data_ingestion"]
        self.bucket_name=self.config["bucket_name"]
        self.bucket_file_name=self.config["bucket_file_name"]
        self.train_test_ratio=self.config["train_ratio"]
        os.makedirs(RAW_DIR,exist_ok=True)
        logger.info(f"Data Ingestion started with {self.bucket_name} and file name {self.bucket_file_name}")
    def download_csv_from_gcp(self):
        try:
            client=storage.Client()
            bucket=client.bucket(self.bucket_name)
            blob=bucket.blob(self.bucket_file_name)
            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"Raw File Downloaded and saved to {RAW_FILE_PATH}")
        except Exception as e:
            logger.error("Error in saving file")
            raise CustomException ("Failed to download",e)
    def split_data(self):
        try:
            logger.info("starting Raw Splitting")
            data=pd.read_csv(RAW_FILE_PATH)
            train_data,test_data=train_test_split(data,test_size=1-self.train_test_ratio,random_state=34)
            train_data.to_csv(TRAIN_FILE_PATH)
            test_data.to_csv(TEST_FILE_PATH)
            logger.info("Splitted Raw data to Train Test Split")
        except Exception as e:
            logger.error("Error in Split")
            raise CustomException ("Failed to split",e)

    def run(self):
        try:
            logger.info("Starting DataINgestion RUN")
            self.download_csv_from_gcp()
            self.split_data()
            logger.info("Data Ingestion Run complete")
        except CustomException as ce:
            logger.error (f"Custom Exec : {str(ce)}")
        finally:
            logger.info("data ingestion complete")

if __name__=="__main__":
    obj=DatIngestion(read_yaml(CONFIG_PATH))
    obj.run()

