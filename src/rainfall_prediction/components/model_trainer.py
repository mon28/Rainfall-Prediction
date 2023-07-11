import os
import sys
import pandas as pd
from catboost import CatBoostClassifier
import joblib
from rainfall_prediction.logging import logger
from rainfall_prediction.app_exception.exception_handler import AppException
from rainfall_prediction.config.configuration import ModelTrainerConfig


class ModelTrainer(object):
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def load_dataset(self):
        try:
            data = pd.read_pickle(self.config.data_filepath)
            logger.info(f"Loaded training data for training of shape {data.shape}")

            X = data.drop(["RainTomorrow"], axis=1)
            y = data["RainTomorrow"]
            return X, y
        except Exception as e:
            raise AppException(e, sys) from e
    

    def train(self):
        try:
            # load dataset
            X, y = self.load_dataset()

            # train model
            model = CatBoostClassifier(iterations=self.config.max_iterations, 
                                            eval_metric=self.config.eval_metric)
            model.fit(X, y)

            # export model to disk
            joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
            logger.info(f"Saving final CatBoost model to {self.config.root_dir}")

        except Exception as e:
            raise AppException(e, sys) from e

