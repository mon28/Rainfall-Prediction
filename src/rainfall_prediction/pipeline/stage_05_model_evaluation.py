from rainfall_prediction.config.configuration import ConfigurationManager
from rainfall_prediction.components.model_evaluation import ModelEvaluation

class ModelEvaluationTrainingPipeline(object):
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.evaluate()