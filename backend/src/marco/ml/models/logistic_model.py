from sklearn.linear_model import LogisticRegression

from marco.ml.models.base import BaseModel


class LogisticModel(BaseModel):

    def build(self):

        return LogisticRegression(
            max_iter=3000,
            random_state=42,
        )