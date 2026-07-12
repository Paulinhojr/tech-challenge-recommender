from recommender.preprocessing.strategy import (
    PreprocessingStrategy,
)


class Trainer:
    def __init__(self, preprocessor: PreprocessingStrategy) -> None:
        self.preprocessor = preprocessor
