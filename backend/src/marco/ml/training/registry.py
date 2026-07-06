from marco.ml.models.catboost_model import CatBoostModel
from marco.ml.models.lightgbm_model import LightGBMModel
from marco.ml.models.logistic_model import LogisticModel
from marco.ml.models.random_forest_model import RandomForestModel
from marco.ml.models.xgboost_model import XGBoostModel


class ModelRegistry:

    def all_models(self):

        return {
            "XGBoost": XGBoostModel().build(),
            "LightGBM": LightGBMModel().build(),
            "CatBoost": CatBoostModel().build(),
            "RandomForest": RandomForestModel().build(),
            "LogisticRegression": LogisticModel().build(),
        }