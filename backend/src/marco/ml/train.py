from time import perf_counter

from joblib import dump

from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

from marco.config.settings import MODELS_DIR
from marco.ml.preprocessing.preprocessor import DataPreprocessor
from marco.ml.training.loader import DatasetLoader
from marco.ml.training.registry import ModelRegistry
from marco.ml.training.splitter import DatasetSplitter


def main():

    print("=" * 70)
    print("MARCO AI TRAINING PIPELINE")
    print("=" * 70)

    df = DatasetLoader().load()

    X_train, X_test, y_train, y_test = DatasetSplitter().split(df)

    registry = ModelRegistry()

    leaderboard = []

    best_pipeline = None
    best_score = 0

    for name, model in registry.all_models().items():

        print(f"\nTraining {name}...")

        pipeline = Pipeline(
            [
                (
                    "preprocessor",
                    DataPreprocessor().build(),
                ),
                (
                    "model",
                    model,
                ),
            ]
        )

        start = perf_counter()

        pipeline.fit(X_train, y_train)

        elapsed = perf_counter() - start

        predictions = pipeline.predict(X_test)

        score = accuracy_score(
            y_test,
            predictions,
        )

        leaderboard.append(
            (
                name,
                score,
                elapsed,
            )
        )

        if score > best_score:
            best_score = score
            best_pipeline = pipeline

    leaderboard.sort(
        key=lambda x: x[1],
        reverse=True,
    )

    print()
    print("=" * 70)
    print("MODEL LEADERBOARD")
    print("=" * 70)

    for rank, (name, score, elapsed) in enumerate(
        leaderboard,
        start=1,
    ):

        print(
            f"{rank}. "
            f"{name:<20}"
            f"{score:.4f}"
            f"   ({elapsed:.2f}s)"
        )

    MODELS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    dump(
        best_pipeline,
        MODELS_DIR / "best_model.joblib",
    )

    print()
    print("=" * 70)
    print(f"🏆 BEST MODEL : {leaderboard[0][0]}")
    print(f"Accuracy     : {leaderboard[0][1]:.4f}")
    print("Saved        : best_model.joblib")
    print("=" * 70)


if __name__ == "__main__":
    main()