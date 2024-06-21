import logging
import datetime

import pandas as pd
from flask_context_manager import Service
import joblib
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

from src.main.resources.objects.data_to_predict import DataToPredict
import logging

logging.basicConfig(level=logging.INFO)


@Service
class PredictionService:
    keras_model = load_model('models/dense_64_32_11_mse_v1.1.keras')
    scaler: StandardScaler = joblib.load('models/scaler.pkl')

    def predict(self, data: list[dict]):

        start = datetime.datetime.now()
        data_to_convert = pd.DataFrame([DataToPredict(**d).model_dump() for d in data])
        scaled_data = self.scaler.transform(data_to_convert)
        result = self.keras_model.predict(scaled_data).tolist()

        result_set: list[dict] = []
        for data_to_convert in result:
            result_set.append({
                'consumoEspecificoTG1_1': data_to_convert[0],
                'consumoEspecificoTG1_2': data_to_convert[1],
                'consumoEspecificoTG2_1': data_to_convert[2],
                'consumoEspecificoTG2_2': data_to_convert[3],
                'potenciaGeradaTG1_1': data_to_convert[4],
                'potenciaGeradaTG1_2': data_to_convert[5],
                'potenciaGeradaTG2_1': data_to_convert[6],
                'potenciaGeradaTG2_2': data_to_convert[7],
                'vazaoVaporEscape': data_to_convert[8]
            })

        difference = datetime.datetime.now() - start
        logging.info(f"Prediction took {difference.total_seconds() * 1000 :.2f} (ms) for {len(data)} samples.")
        return result_set
