import os
import sys
from rainfall_prediction.logging import logger
from rainfall_prediction.app_exception.exception_handler import AppException
from rainfall_prediction.entity import DataIngestionConfig


class DataValidation(object):
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def validate_data_file_exists(self) -> bool:
        try:
            validation_status = None

            required_filepath = os.listdir(os.path.join(*["artifacts", "data_ingestion", "rainfall_australia_dataset"]))

            for file in required_filepath:
                if file not in self.config.REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            logger.info(f"Status file updated with validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise AppException(e, sys) from e