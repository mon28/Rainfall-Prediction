import os
import sys
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import confusion_matrix, classification_report
from rainfall_prediction.logging import logger
from rainfall_prediction.app_exception.exception_handler import AppException
from rainfall_prediction.config.configuration import ModelEvaluationConfig


class ModelEvaluation(object):
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config


    def evaluate(self):

        try:
            # load evaluation data
            data = pd.read_pickle(self.config.data_filepath)
            logger.info(f"Loaded data for evaluation of shape {data.shape}")

            X_test = data.drop(["RainTomorrow"], axis=1)
            y_test = data["RainTomorrow"]

            # load Model from disk
            model = joblib.load(os.path.join(self.config.model_path, self.config.model_name))
            logger.info(f"Loaded CatBoost model from {self.config.model_path}")

            # perform evaluation
            y_pred = model.predict(X_test)

            conf_matrix = pd.DataFrame(confusion_matrix(y_test, y_pred))
            clf_report = pd.DataFrame(np.array([classification_report(y_test, y_pred)]))

            # create evaluation report
            conf_matrix.to_csv(self.config.metric_file_name, mode='a', index=False)
            clf_report.to_csv(self.config.metric_file_name, mode='a', index=False)
            
            logger.info(f"Model Evaluation completed successfully! \
                        Evaluation metric report in: {self.config.metric_file_name}")

        except Exception as e:
            raise AppException(e, sys) from e