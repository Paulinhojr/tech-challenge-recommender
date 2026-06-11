from models.base_model import BaseModel
from models.mlp_model import MLPModel


class ModelFactory:
    """
    Factory responsible for creating models.
    """

    @staticmethod
    def create(model_name: str) -> BaseModel:
        """
        Create a model instance.

        Args:
            model_name: Name of the model.

        Returns:
            Instantiated model.

        Raises:
            ValueError: If the model is not supported.
        """

        if model_name.lower() == "mlp":
            return MLPModel()

        raise ValueError(f"Model '{model_name}' not supported.")
