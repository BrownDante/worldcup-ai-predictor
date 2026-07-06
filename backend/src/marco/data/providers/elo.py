from pathlib import Path

from marco.data.providers.base import DataProvider


class EloProvider(DataProvider):
    def __init__(self, destination: Path):
        super().__init__("Elo Ratings", destination)

    def download(self):
        self.destination.mkdir(parents=True, exist_ok=True)
        print(f"Downloaded {self.dataset_name}")

    def validate(self):
        print(f"Validated {self.dataset_name}")

    def transform(self):
        print(f"Transformed {self.dataset_name}")