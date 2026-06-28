# STAGE 1: Builder (Instalação com UV)

FROM python:3.11-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalar o uv (ferramenta usada na Etapa 2)
RUN pip install uv

# Copiar os arquivos de dependência
COPY pyproject.toml uv.lock ./

# Criar ambiente virtual, instalar as bibliotecas do amigo E também o dvc
RUN uv venv && uv pip install -r pyproject.toml dvc


# STAGE 2: Runtime (Imagem final leve)
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copiar o ambiente virtual pronto do Stage 1
COPY --from=builder /app/.venv /app/.venv

# Colocar o ambiente virtual no PATH do sistema
ENV PATH="/app/.venv/bin:$PATH"

# Copiar o restante do código do projeto
COPY . .

# Truque para manter o contêiner ligado rodando em segundo plano
CMD ["tail", "-f", "/dev/null"]