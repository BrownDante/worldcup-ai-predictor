from pathlib import Path
import shutil

import kagglehub

from marco.data.providers.base import DataProvider


class HistoricalMatchesProvider(DataProvider):
    def __init__(self, destination: Path):
        super().__init__("Historical Matches", destination)

    def download(self):
        print("Downloading historical dataset...")

        dataset_path = Path(
            kagglehub.dataset_download(
                "martj42/international-football-results-from-1872-to-2017"
            )
        )

        self.destination.mkdir(parents=True, exist_ok=True)

        files = [
            "results.csv",
            "goalscorers.csv",
            "shootouts.csv",
            "former_names.csv",
        ]

        for file in files:
            src = dataset_path / file
            dst = self.destination / file

            shutil.copy2(src, dst)

            print(f"Copied {file}")

    def validate(self):
        print("Validated Historical Matches")

    def transform(self):
        print("Transformed Historical Matches")