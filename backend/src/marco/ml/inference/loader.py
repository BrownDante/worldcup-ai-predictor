import joblib


class ModelLoader:

    @staticmethod
    def load(path):

        return joblib.load(path)