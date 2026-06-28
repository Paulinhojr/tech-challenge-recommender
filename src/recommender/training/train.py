import mlflow
import os
from pathlib import Path
import socket 

def main():
    # 1. Configurar a ligação ao servidor MLflow (Traduzindo o nome para IP para driblar o bloqueio)
    try:
        mlflow_ip = socket.gethostbyname("mlflow_server")
        mlflow_uri = f"http://{mlflow_ip}:5000"
    except Exception:
        mlflow_uri = "http://localhost:5000"
        
    mlflow.set_tracking_uri(mlflow_uri)
    
    # 2. Definir o nome do experimento
    mlflow.set_experiment("Recommender_System_Experiment")
    
    print("A iniciar o rastreamento no MLflow...")

    # 3. Iniciar o registo (Run)
    with mlflow.start_run():
        
        # ZONA (ETAPA 4 - PyTorch)
        # Carregar os dados do DVC e treinar a rede
        
        # Exemplo de Rastreamento de PARÂMETROS
        # Substituir pelos hiperparâmetros reais da rede dele
        mlflow.log_param("learning_rate", 0.001)
        mlflow.log_param("epochs", 10)
        mlflow.log_param("batch_size", 32)
        
        # Exemplo de Rastreamento de MÉTRICAS
        # Colocar isto dentro do loop de treino (loss, accuracy, etc.)
        mlflow.log_metric("train_loss", 0.45)
        mlflow.log_metric("val_loss", 0.48)
        

        # SALVAGUARDA DOS ARTEFATOS
        output_dir = Path("artifacts")
        output_dir.mkdir(parents=True, exist_ok=True)
        model_path = output_dir / "model.pt"
        
        with open(model_path, "w") as f:
            f.write("Os pesos do modelo PyTorch (Etapa 4) serão guardados aqui.")
            
        mlflow.log_artifact(str(model_path))
        
        print("Treino simulado concluído! Parâmetros, métricas e artefatos registados no MLflow.")

if __name__ == "__main__":
    main()