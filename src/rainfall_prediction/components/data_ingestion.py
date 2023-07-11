import os
import sys
import urllib.request as request
import zipfile
from pathlib import Path
from rainfall_prediction.logging import logger
from rainfall_prediction.app_exception.exception_handler import AppException
from rainfall_prediction.utils.common import get_size
from rainfall_prediction.entity import DataIngestionConfig

class DataIngestion(object):
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    self.config.source_URL,
                    filename=self.config.local_data_file                    
                )
                logger.info(f"{filename} downloaded with the following info: \n{headers}")
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
        except Exception as e:
            raise AppException(e, sys) from e


    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            if zipfile.is_zipfile(self.config.local_data_file):
                with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                    zip_ref.extractall(unzip_path)
                logger.info(f"Extracted datafile to {unzip_path}.")
            else:
                logger.info(f"{self.config.local_data_file} is not a zip file.")
        except Exception as e:
            raise AppException(e, sys) from e