import numpy as np
from pydantic import BaseModel


class DataToPredict(BaseModel):

    vazaoVapor: float
    pressaoVapor: float
    temperaturaVapor: float
    cargaVaporTG1: float
    cargaVaporTG2: float
    habilitaTG1: float
    habilitaTG2: float

    def to_array(self):
        return np.array([
            self.vazaoVapor,
            self.pressaoVapor,
            self.temperaturaVapor,
            self.cargaVaporTG1,
            self.cargaVaporTG2,
            self.habilitaTG1,
            self.habilitaTG2
        ]).reshape(1, -1)

    def to_pandas(self):
        import pandas as pd
        return pd.DataFrame([self.dict()])
