from models.base_model import BaseModel


class MLPModel(BaseModel):
    """
    Simple MLP recommendation model.
    """

    def train(self) -> None:
        """
        Train the MLP model.
        """

        print("Training MLP model...")
