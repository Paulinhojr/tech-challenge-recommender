import pandas as pd
from sklearn.preprocessing import StandardScaler

from recommender.preprocessing.strategy import (
    PreprocessingStrategy,
)


class StandardScalerStrategy(PreprocessingStrategy):
    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        scaler = StandardScaler()

        scaled_data = scaler.fit_transform(data)

        return pd.DataFrame(
            scaled_data,
            columns=data.columns,
        )
