from abc import ABC, abstractmethod


class BaseModel(ABC):
    """
    Base class for all recommendation models.
    """

    @abstractmethod
    def train(self) -> None:
        """
        Train the model.
        """
        pass
