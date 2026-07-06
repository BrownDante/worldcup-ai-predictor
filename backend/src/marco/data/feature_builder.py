from marco.data.elo_engine import EloEngine
from marco.data.rolling_stats import RollingStats
from marco.data.head_to_head import HeadToHead
import pandas as pd


class FeatureBuilder:

    def build(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        df = df.sort_values("date").reset_index(drop=True)

        team_history = {}

        home_form = []
        away_form = []

        home_attack = []
        away_attack = []

        home_defence = []
        away_defence = []

        for _, row in df.iterrows():

            home = row.home_team
            away = row.away_team

            if home not in team_history:
                team_history[home] = []

            if away not in team_history:
                team_history[away] = []

            last_home = team_history[home][-5:]
            last_away = team_history[away][-5:]

            def avg(matches, key):
                if not matches:
                    return 0.0
                return sum(m[key] for m in matches) / len(matches)

            def wins(matches):
                if not matches:
                    return 0
                return sum(m["win"] for m in matches)

            home_form.append(wins(last_home))
            away_form.append(wins(last_away))

            home_attack.append(avg(last_home, "gf"))
            away_attack.append(avg(last_away, "gf"))

            home_defence.append(avg(last_home, "ga"))
            away_defence.append(avg(last_away, "ga"))

            team_history[home].append(
                {
                    "gf": row.home_score,
                    "ga": row.away_score,
                    "win": int(row.home_score > row.away_score),
                }
            )

            team_history[away].append(
                {
                    "gf": row.away_score,
                    "ga": row.home_score,
                    "win": int(row.away_score > row.home_score),
                }
            )

        df["home_form"] = home_form
        df["away_form"] = away_form

        df["home_attack"] = home_attack
        df["away_attack"] = away_attack

        df["home_defence"] = home_defence
        df["away_defence"] = away_defence

        df["home_advantage"] = (~df["neutral"]).astype(int)

        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month

        # Prediction target
        def match_result(row):
            if row.home_score > row.away_score:
                return 2
            elif row.home_score < row.away_score:
                return 0
            else:
                return 1
        df["target"] = df.apply(
            match_result,
            axis=1,
        )
        

        elo = EloEngine()
        df = elo.transform(df)

        df = RollingStats().transform(df)

        df = HeadToHead().transform(df)

        return df