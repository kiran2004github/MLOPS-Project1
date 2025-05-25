from src.custom_exception import CustomException
from src.logger import get_logger
import sys

logger=get_logger(__name__)

def div(a:int,b:int):
    try:
        c=a/b
        logger.info("div a and b")
        return c
    except Exception as e:
        logger.error("Error occured")
        raise CustomException(error_message="Divide by zero Not possible",error_details=sys)
if __name__=="__main__":
    try :
        logger.info("Main Start")
        div(2,0)
    except CustomException as ce:
        logger.error(str(ce))