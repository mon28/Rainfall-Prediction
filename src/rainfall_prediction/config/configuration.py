from rainfall_prediction.constants import *
from rainfall_prediction.utils.common import read_yaml, create_directories
from rainfall_prediction.entity import (DataIngestionConfig,
                                        DataValidationConfig,
                                        DataTransformationConfig,
                                        ModelTrainerConfig,
                                        ModelEvaluationConfig,
                                        ModelInferenceConfig)


class ConfigurationManager(object):
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            REQUIRED_FILES=config.REQUIRED_FILES,
            STATUS_FILE=config.STATUS_FILE
        )
        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_filepath=config.data_filepath,
            train_data_filename=config.train_data_filename,
            eval_data_filename=config.eval_data_filename
        )
        return data_transformation_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_training
        params = self.params.model_training

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            model_name=config.model_name,
            data_filepath=config.data_filepath,
            max_iterations=params.max_iterations,
            eval_metric=params.eval_metric
        )
        return model_trainer_config
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_filepath=config.data_filepath,
            model_path=config.model_path,
            model_name=config.model_name,
            metric_file_name=config.metric_file_name
        )
        return model_evaluation_config
    

    def get_model_inference_config(self) -> ModelInferenceConfig:
        config = self.config.model_inference

        model_inference_config = ModelInferenceConfig(
            model_filepath=config.model_filepath
        )
        return model_inference_config
