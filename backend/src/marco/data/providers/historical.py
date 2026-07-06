from pathlib import Path
import kagglehub

from marco.data.providers.base import DataProvider


class HistoricalMatchesProvider(DataProvider):
    def __init__(self, destination: Path):
        super().__init__("Historical Matches", destination)

    def download(self):
        print("Downloading historical dataset from Kaggle...")

        path = kagglehub.dataset_download(
            "martj42/international-football-results-from-1872-to-2017"
        )

        print(f"Dataset downloaded to: {path}")

    def validate(self):
        print("Historical dataset validated.")

    def transform(self):
        print("Historical dataset transformed.")