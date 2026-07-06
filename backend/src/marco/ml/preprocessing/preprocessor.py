from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


class DataPreprocessor:

    def build(self):

        categorical_features = [
            "home_team",
            "away_team",
            "tournament",
            "country",
        ]

        numeric_features = [
            "home_form",
            "away_form",
            "home_attack",
            "away_attack",
            "home_defence",
            "away_defence",
            "home_elo",
            "away_elo",
            "elo_difference",
            "home_last5_winrate",
            "away_last5_winrate",
            "home_last5_goals",
            "away_last5_goals",
            "home_last5_conceded",
            "away_last5_conceded",
            "home_h2h_wins",
            "away_h2h_wins",
            "h2h_draws",
            "home_advantage",
            "year",
            "month",
        ]

        preprocessor = ColumnTransformer(
            transformers=[
                (
                    "cat",
                    OneHotEncoder(
                        handle_unknown="ignore"
                    ),
                    categorical_features,
                ),
                (
                    "num",
                    "passthrough",
                    numeric_features,
                ),
            ]
        )

        return preprocessor