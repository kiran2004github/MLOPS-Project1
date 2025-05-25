from src.data_ingestion import DatIngestion
from src.datapreprocessing import DataProcessor
from src.model_training import modelTraining
from utils.common_functions import read_yaml
from config.paths_config import *

if __name__ =="__main__":
    data=DatIngestion(read_yaml(CONFIG_PATH))
    data.run()
    processor=DataProcessor(train_path=TRAIN_FILE_PATH,test_path=TEST_FILE_PATH,processed_dir=PROCESSSED_DIR,config_path=CONFIG_PATH)
    processor.process()
    trainer=modelTraining(train_path=PROCESSED_TRAIN_DATA_PATH,test_path=PROCESSED_TEST_DATA_PATH,model_out_path=MODEL_OUTPUT_PATH)
    trainer.run()
    