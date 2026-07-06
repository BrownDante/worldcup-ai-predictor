import pandas as pd


class HeadToHead:

    def transform(self, df: pd.DataFrame):

        df = df.copy()
        history = {}

        home_h2h_wins = []
        away_h2h_wins = []
        h2h_draws = []

        for _, row in df.iterrows():

            home = row.home_team
            away = row.away_team

            key = tuple(sorted([home, away]))

            if key not in history:
                history[key] = []

            matches = history[key]

            hw = 0
            aw = 0
            dr = 0

            for m in matches:

                if m["winner"] == "draw":
                    dr += 1

                elif m["winner"] == home:
                    hw += 1

                elif m["winner"] == away:
                    aw += 1

            home_h2h_wins.append(hw)
            away_h2h_wins.append(aw)
            h2h_draws.append(dr)

            if row.home_score > row.away_score:
                winner = home

            elif row.home_score < row.away_score:
                winner = away

            else:
                winner = "draw"

            history[key].append({"winner": winner})

        df["home_h2h_wins"] = home_h2h_wins
        df["away_h2h_wins"] = away_h2h_wins
        df["h2h_draws"] = h2h_draws

        return df