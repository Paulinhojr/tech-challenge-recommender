import json
from pathlib import Path

import pandas as pd


def main() -> None:
    """Gera métricas básicas para manter o pipeline DVC funcional."""

    print("Iniciando avaliação básica do pipeline...")

    features_path = Path("data/processed/features.csv")
    model_path = Path("artifacts/model.pt")
    output_path = Path("artifacts/metrics.json")

    df = pd.read_csv(features_path)

    # Métricas básicas da Etapa 3 para validar a execução do pipeline.
    # TODO(Etapa 4): substituir por métricas reais do modelo final,
    # como accuracy, precision, recall, f1-score, RMSE ou ranking metrics.
    metrics = {
        "num_interactions": int(len(df)),
        "mean_rating": float(df["rating"].mean()) if "rating" in df.columns else 0.0,
        "model_artifact_exists": int(model_path.exists()),
    }

    if "liked" in df.columns:
        metrics["positive_rate"] = float(df["liked"].mean())

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=4)

    print(f"Sucesso! Métricas salvas em {output_path}")


if __name__ == "__main__":
    main()