from src.recommender.config.settings import settings


def validate() -> None:
    print("APP_ENV:", settings.app_env)
    print("DATA_PATH:", settings.data_path)
    print("MODEL_PATH:", settings.model_path)
    print("MLFLOW_TRACKING_URI:", settings.mlflow_tracking_uri)
    print("RANDOM_SEED:", settings.random_seed)


if __name__ == "__main__":
    validate()
