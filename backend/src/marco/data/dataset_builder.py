from pathlib import Path

import pandas as pd


class DatasetBuilder:

    def __init__(self, output_dir: Path):

        self.output_dir = output_dir

    def save(self, df: pd.DataFrame):

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_parquet(
            self.output_dir / "training_dataset.parquet",
            index=False,
        )

        print()

        print("Training dataset saved")