import os
import pandas
import yaml
from src.logger import get_logger
from src.custom_exception import CustomException
import pandas as pd
logger=get_logger(__name__)
def read_yaml(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("File Not in the Path")
        with open(path,'r') as f:
            config=yaml.safe_load(f)
            logger.info("Successfully loaded config")
            return config
    except Exception as e:
        logger.error("Error reading Config")
        raise CustomException(error_message="Failed to read config",error_details=e)
def load_data(path):
    try:
        logger.info("Loading data for Preprocessing")
        return pd.read_csv(path)
    except Exception as e:
        logger.error("Error Loading data")
        raise CustomException (error_message="Error loading",error_detail=e)
