from flask_context_manager import Controller, rest_mapping, post_mapping

from src.main.service.prediction import PredictionService


@Controller
@rest_mapping('/api/v1')
class PredictionController:

    def __init__(self, service: PredictionService):
        self.service = service

    @post_mapping('/predict')
    def predict(self, data: list[dict]):
        return self.service.predict(data)
