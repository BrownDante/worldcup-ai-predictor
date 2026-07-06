from sklearn.model_selection import train_test_split


class DatasetSplitter:

    def split(self, df):

        X = df.drop(
            columns=[
                "target",
                "date",
                "home_score",
                "away_score",
                "neutral",
            ]
        )

        y = df["target"]

        return train_test_split(
            X,
            y,
            test_size=0.20,
            shuffle=False,
            random_state=42,
        )