from pathlib import Path

import pandas as pd

from marco.config.settings import DATA_DIR


class DatasetLoader:

    def __init__(self):

        self.dataset = (
            DATA_DIR
            / "processed"
            / "training_dataset.parquet"
        )

    def load(self) -> pd.DataFrame:

        print(f"Loading dataset: {self.dataset}")

        return pd.read_parquet(self.dataset)