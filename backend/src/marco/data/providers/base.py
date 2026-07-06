from abc import ABC, abstractmethod
from pathlib import Path


class DataProvider(ABC):
    def __init__(self, dataset_name: str, destination: Path):
        self.dataset_name = dataset_name
        self.destination = destination

    @abstractmethod
    def download(self):
        ...

    @abstractmethod
    def validate(self):
        ...

    @abstractmethod
    def transform(self):
        ...