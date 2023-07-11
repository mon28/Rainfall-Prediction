from rainfall_prediction.config.configuration import ConfigurationManager
from rainfall_prediction.components.model_inference import ModelInference

class ModelPrediction(object):
    def __init__(self):
        pass

    def predict(self, input_params):
        config = ConfigurationManager()
        model_inference_config = config.get_model_inference_config()
        model_infence = ModelInference(model_inference_config)
        return model_infence.predict(input_params)