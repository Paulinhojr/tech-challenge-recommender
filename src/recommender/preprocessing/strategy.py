from abc import ABC, abstractmethod

import pandas as pd


class PreprocessingStrategy(ABC):
    """
    Base preprocessing strategy.
    """

    @abstractmethod
    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Process data.
        """
