import sys
import joblib
from rainfall_prediction.logging import logger
from rainfall_prediction.app_exception.exception_handler import AppException
from rainfall_prediction.config.configuration import ModelInferenceConfig


class ModelInference(object):
    def __init__(self, config: ModelInferenceConfig):
        self.config = config

    
    def predict(self, input_params):
        try:
            # load Model from disk
            model = joblib.load(self.config.model_filepath)
            logger.info(f"Loaded CatBoost model from {self.config.model_filepath}")

            return model.predict(input_params)
        except Exception as e:
            raise AppException(e, sys) from e
        
        