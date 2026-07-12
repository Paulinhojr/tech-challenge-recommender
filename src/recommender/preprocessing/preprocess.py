import pandas as pd
from pathlib import Path

def load_data(file_path: Path) -> pd.DataFrame:
    """Carrega o dataset bruto de avaliações.

    Args:
        file_path (Path): Caminho para o arquivo CSV bruto.

    Returns:
        pd.DataFrame: DataFrame contendo os dados carregados.
    """
    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove valores nulos e colunas desnecessárias do dataset.

    Args:
        df (pd.DataFrame): DataFrame bruto.

    Returns:
        pd.DataFrame: DataFrame limpo apenas com colunas essenciais.
    """
    df_cleaned = df.dropna().copy()
    
    # O timestamp não será usado no modelo básico de recomendação MLP
    if 'timestamp' in df_cleaned.columns:
        df_cleaned = df_cleaned.drop(columns=['timestamp'])
        
    return df_cleaned

def encode_ids(df: pd.DataFrame) -> pd.DataFrame:
    """Mapeia IDs originais para índices contínuos (0 a N-1) para o PyTorch.

    Args:
        df (pd.DataFrame): DataFrame limpo com IDs originais.

    Returns:
        pd.DataFrame: DataFrame com as novas colunas 'user_idx' e 'item_idx'.
    """
    df_encoded = df.copy()
    
    # Transforma os IDs em variáveis categóricas e extrai os códigos sequenciais
    df_encoded['user_idx'] = df_encoded['userId'].astype('category').cat.codes
    df_encoded['item_idx'] = df_encoded['movieId'].astype('category').cat.codes
    
    return df_encoded

def main() -> None:
    """Executa o pipeline completo de pré-processamento."""
    
    # Caminhos baseados na nossa estrutura de pastas e no dvc.yaml
    input_path = Path("data/MovieLens 100k/ml-latest-small/ratings.csv")
    output_dir = Path("data/processed")
    output_path = output_dir / "ratings_cleaned.csv"

    print("Iniciando o pré-processamento dos dados...")

    # Garante que a pasta de saída exista antes de salvar
    output_dir.mkdir(parents=True, exist_ok=True)

    # Execução encadeada do pipeline
    df_raw = load_data(input_path)
    df_clean = clean_data(df_raw)
    df_final = encode_ids(df_clean)

    # Salva o CSV processado sem o índice do Pandas
    df_final.to_csv(output_path, index=False)
    
    print(f"Sucesso! Dados mastigados e salvos em: {output_path}")

if __name__ == "__main__":
    main()