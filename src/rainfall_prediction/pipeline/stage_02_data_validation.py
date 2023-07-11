from rainfall_prediction.config.configuration import ConfigurationManager
from rainfall_prediction.components.data_validation import DataValidation

class DataValidationTrainingPipeline(object):
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_data_file_exists()
