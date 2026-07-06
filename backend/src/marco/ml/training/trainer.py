from xgboost import XGBClassifier


class ModelTrainer:

    def train(self, X_train, y_train):

        model = XGBClassifier(
            n_estimators=300,
            max_depth=6,
            learning_rate=0.05,
            random_state=42,
            eval_metric="logloss",
        )

        model.fit(
            X_train,
            y_train,
        )

        return model