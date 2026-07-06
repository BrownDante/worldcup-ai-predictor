from sklearn.preprocessing import LabelEncoder


class EncoderManager:

    def __init__(self):
        self.encoders = {}

    def fit_transform(self, df, columns):

        df = df.copy()

        for column in columns:

            encoder = LabelEncoder()

            df[column] = encoder.fit_transform(
                df[column].astype(str)
            )

            self.encoders[column] = encoder

        return df

    def transform(self, df, columns):

        df = df.copy()

        for column in columns:

            df[column] = self.encoders[column].transform(
                df[column].astype(str)
            )

        return df