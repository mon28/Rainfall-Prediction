from rainfall_prediction.config.configuration import ConfigurationManager
from rainfall_prediction.components.model_trainer import ModelTrainer

class ModelTrainerTrainingPipeline(object):
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()