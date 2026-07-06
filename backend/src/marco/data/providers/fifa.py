from pathlib import Path

from marco.data.providers.base import DataProvider


class FIFAProvider(DataProvider):

    def __init__(self, destination: Path):
        super().__init__(
            dataset_name="FIFA Rankings",
            destination=destination,
        )

    def download(self):
        print(f"Downloading {self.dataset_name}")

    def validate(self):
        print(f"Validating {self.dataset_name}")

    def transform(self):
        print(f"Transforming {self.dataset_name}")