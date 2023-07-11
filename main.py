from rainfall_prediction.logging import logger
from rainfall_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from rainfall_prediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from rainfall_prediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from rainfall_prediction.pipeline.strage_04_model_training import ModelTrainerTrainingPipeline
from rainfall_prediction.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


class TrainingPipeline(object):
    def __init__(self):
        pass

    def start_training_pipeline(self):
        self.data_ingestion_stage()
        self.data_validation_stage()
        self.data_transformation_stage()
        self.model_training_stage()
        self.model_evaluation_stage()

    def data_ingestion_stage(self):
        STAGE_NAME = "Data Ingestion Stage"
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            data_ingestion = DataIngestionTrainingPipeline()
            data_ingestion.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx============================x")
        except Exception as e:
            logger.exception(e)
            raise e

    def data_validation_stage(self):
        STAGE_NAME = "Data Validation Stage"
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            data_validation = DataValidationTrainingPipeline()
            data_validation.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx============================x")
        except Exception as e:
            logger.exception(e)
            raise e
        
    def data_transformation_stage(self):
        STAGE_NAME = "Data Tranformation Stage"
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            data_transformation = DataTransformationTrainingPipeline()
            data_transformation.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx============================x")
        except Exception as e:
            logger.exception(e)
            raise e
        
    def model_training_stage(self):
        STAGE_NAME = "Model Trainer Stage"
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            model_training = ModelTrainerTrainingPipeline()
            model_training.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx============================x")
        except Exception as e:
            logger.exception(e)
            raise e
        
    def model_evaluation_stage(self):
        STAGE_NAME = "Model Evaluation Stage"
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            model_evaluation = ModelEvaluationTrainingPipeline()
            model_evaluation.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx============================x")
        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == "__main__":
    trainingPipeline = TrainingPipeline()
    trainingPipeline.start_training_pipeline()