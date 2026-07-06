from pathlib import Path

import pandas as pd


class DataCleaner:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir

    def clean_results(self) -> pd.DataFrame:

        csv = self.data_dir / "historical" / "results.csv"

        if not csv.exists():
            raise FileNotFoundError(f"Dataset not found: {csv}")

        df = pd.read_csv(csv)

        print(f"Loaded {len(df):,} matches")

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Parse dates
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

        # Convert scores to numeric
        df["home_score"] = pd.to_numeric(
            df["home_score"],
            errors="coerce",
        )

        df["away_score"] = pd.to_numeric(
            df["away_score"],
            errors="coerce",
        )

        # Drop invalid rows
        df = df.dropna(
            subset=[
                "date",
                "home_score",
                "away_score",
            ]
        )

        # Convert to integers
        df["home_score"] = df["home_score"].astype(int)
        df["away_score"] = df["away_score"].astype(int)

        # Clean text columns
        text_columns = [
            "home_team",
            "away_team",
            "tournament",
            "city",
            "country",
        ]

        for column in text_columns:
            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
            )

        # Ensure neutral column is bool
        df["neutral"] = df["neutral"].astype(bool)

        print(f"After cleaning: {len(df):,} matches")

        return df