from rainfall_prediction.config.configuration import ConfigurationManager
from rainfall_prediction.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline(object):
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.transform_data()