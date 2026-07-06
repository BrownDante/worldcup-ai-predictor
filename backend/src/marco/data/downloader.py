from marco.config.settings import DATA_DIR

from marco.data.providers.historical import HistoricalMatchesProvider
from marco.data.providers.fifa import FIFAProvider
from marco.data.providers.elo import EloProvider


class DownloadManager:
    def __init__(self):
        self.providers = [
            HistoricalMatchesProvider(DATA_DIR / "raw" / "historical"),
            FIFAProvider(DATA_DIR / "raw" / "rankings"),
            EloProvider(DATA_DIR / "raw" / "elo"),
        ]

    def run(self):
        for provider in self.providers:
            print("-" * 50)
            provider.download()
            provider.validate()
            provider.transform()


if __name__ == "__main__":
    DownloadManager().run()