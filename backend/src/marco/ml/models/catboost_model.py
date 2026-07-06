from catboost import CatBoostClassifier

from marco.ml.models.base import BaseModel


class CatBoostModel(BaseModel):

    def build(self):

        return CatBoostClassifier(

    loss_function="MultiClass",

    verbose=False,

    random_state=42,
)