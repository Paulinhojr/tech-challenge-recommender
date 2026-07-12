from models.model_factory import ModelFactory


def main() -> None:
    model = ModelFactory.create("mlp")

    model.train()


if __name__ == "__main__":
    main()
