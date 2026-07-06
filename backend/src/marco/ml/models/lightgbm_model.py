from lightgbm import LGBMClassifier

from marco.ml.models.base import BaseModel


class LightGBMModel(BaseModel):

    def build(self):

        return LGBMClassifier(

    objective="multiclass",

    num_class=3,

    random_state=42,
)