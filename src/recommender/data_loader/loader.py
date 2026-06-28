from pathlib import Path

import pandas as pd


class DataLoader:
    """
    Responsible only for loading datasets.
    """

    @staticmethod
    def load_csv(file_path: Path) -> pd.DataFrame:
        """
        Load CSV dataset.

        Args:
            file_path: Path to csv file.

        Returns:
            Loaded dataframe.
        """

        return pd.read_csv(file_path)
