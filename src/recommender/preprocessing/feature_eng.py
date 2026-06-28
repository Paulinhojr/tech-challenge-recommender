from pathlib import Path

import pandas as pd


def main() -> None:
    """Gera o arquivo de features para o pipeline DVC."""

    print("Iniciando Feature Engineering...")

    input_path = Path("data/processed/ratings_cleaned.csv")
    output_path = Path("data/processed/features.csv")

    df = pd.read_csv(input_path)

    # Métricas temporárias para manter o pipeline DVC funcional.
    # TODO(Etapa 4): substituir por métricas reais do modelo final.
    # para o modelo final de recomendação em PyTorch.
    if "rating" in df.columns:
        df["liked"] = (df["rating"] >= 4.0).astype(int)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Sucesso! Features salvas em {output_path}")


if __name__ == "__main__":
    main()