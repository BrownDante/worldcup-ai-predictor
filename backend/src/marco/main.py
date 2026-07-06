from marco.config.settings import DATA_DIR

from marco.data.cleaner import DataCleaner
from marco.data.feature_builder import FeatureBuilder
from marco.data.dataset_builder import DatasetBuilder


def main():

    cleaner = DataCleaner(DATA_DIR / "raw")

    df = cleaner.clean_results()

    features = FeatureBuilder().build(df)

    DatasetBuilder(
        DATA_DIR / "processed"
    ).save(features)

    print()

    print(features.head())

    print()

    print(features.columns)


if __name__ == "__main__":

    main()