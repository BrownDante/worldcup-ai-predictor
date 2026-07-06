from xgboost import XGBClassifier

from marco.ml.models.base import BaseModel


class XGBoostModel(BaseModel):

    def build(self):

        return XGBClassifier(

            objective="multi:softprob",

            num_class=3,

            eval_metric="mlogloss",

            n_estimators=500,

            max_depth=8,

            learning_rate=0.05,

            subsample=0.9,

            colsample_bytree=0.9,

            random_state=42,
        )