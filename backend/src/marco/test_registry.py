from marco.config.settings import DATA_DIR
from marco.data.cleaner import DataCleaner


def main():
    cleaner = DataCleaner(DATA_DIR / "raw")

    df = cleaner.clean_results()

    print()
    print(df.head())

    print()
    print(df.info())


if __name__ == "__main__":
    main()