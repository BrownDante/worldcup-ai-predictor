import pandas as pd


class EloEngine:

    def __init__(self, k_factor: int = 30):

        self.k = k_factor
        self.ratings = {}

    def rating(self, team: str):

        return self.ratings.get(team, 1500)

    def expected(self, ra, rb):

        return 1 / (1 + 10 ** ((rb - ra) / 400))

    def update(self, winner, loser, draw=False):

        ra = self.rating(winner)
        rb = self.rating(loser)

        ea = self.expected(ra, rb)
        eb = self.expected(rb, ra)

        if draw:
            sa = sb = 0.5
        else:
            sa = 1
            sb = 0

        self.ratings[winner] = ra + self.k * (sa - ea)
        self.ratings[loser] = rb + self.k * (sb - eb)

    def transform(self, df: pd.DataFrame):

        home_elo = []
        away_elo = []

        for _, row in df.iterrows():

            home = row.home_team
            away = row.away_team

            home_elo.append(self.rating(home))
            away_elo.append(self.rating(away))

            if row.home_score > row.away_score:

                self.update(home, away)

            elif row.home_score < row.away_score:

                self.update(away, home)

            else:

                self.update(home, away, draw=True)

        df["home_elo"] = home_elo
        df["away_elo"] = away_elo
        df["elo_difference"] = df.home_elo - df.away_elo

        return df