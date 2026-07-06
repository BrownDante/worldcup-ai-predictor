import pandas as pd


class RollingStats:

    def transform(self, df: pd.DataFrame):

        df = df.copy()
        df = df.sort_values("date").reset_index(drop=True)

        history = {}

        home_last5_winrate = []
        away_last5_winrate = []

        home_last5_goals = []
        away_last5_goals = []

        home_last5_conceded = []
        away_last5_conceded = []

        for _, row in df.iterrows():

            home = row.home_team
            away = row.away_team

            if home not in history:
                history[home] = []

            if away not in history:
                history[away] = []

            def stats(matches):

                if len(matches) == 0:

                    return (
                        0,
                        0,
                        0,
                    )

                last = matches[-5:]

                wins = sum(m["win"] for m in last) / len(last)

                goals = sum(m["gf"] for m in last) / len(last)

                conceded = sum(m["ga"] for m in last) / len(last)

                return wins, goals, conceded

            hw, hg, hc = stats(history[home])

            aw, ag, ac = stats(history[away])

            home_last5_winrate.append(hw)
            away_last5_winrate.append(aw)

            home_last5_goals.append(hg)
            away_last5_goals.append(ag)

            home_last5_conceded.append(hc)
            away_last5_conceded.append(ac)

            history[home].append(
                {
                    "win": int(row.home_score > row.away_score),
                    "gf": row.home_score,
                    "ga": row.away_score,
                }
            )

            history[away].append(
                {
                    "win": int(row.away_score > row.home_score),
                    "gf": row.away_score,
                    "ga": row.home_score,
                }
            )

        df["home_last5_winrate"] = home_last5_winrate
        df["away_last5_winrate"] = away_last5_winrate

        df["home_last5_goals"] = home_last5_goals
        df["away_last5_goals"] = away_last5_goals

        df["home_last5_conceded"] = home_last5_conceded
        df["away_last5_conceded"] = away_last5_conceded

        return df