from sklearn.ensemble import RandomForestClassifier

from marco.ml.models.base import BaseModel


class RandomForestModel(BaseModel):

    def build(self):

        return RandomForestClassifier(
            n_estimators=400,
            random_state=42,
            n_jobs=-1,
        )