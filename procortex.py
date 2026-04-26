# procortex.py

import requests
from config import DEPOSITO_FORNECEDOR

QUESTION_ID = 123  # substituir pelo ID real do card
QUESTION_URL = (
    f"http://metabase.procortex.com.br/public/question/{QUESTION_ID}.json"
)


def buscar_estoque_procortex():
    print("🔄 Buscando dados do Procortex (Metabase)...")

    response = requests.get(QUESTION_URL, timeout=30)

    if response.status_code != 200:
        raise Exception(
            f"Erro ao acessar Procortex: "
            f"{response.status_code} - {response.text}"
        )

    dados = response.json()
    print(f"📦 Total de linhas recebidas: {len(dados)}")

    estoque = {}

    for linha in dados:
        deposito = str(linha.get("deposito")).upper().strip()
        codigo = str(linha.get("cod_fabrica")).strip()
        quantidade = linha.get("quantidade")

        if deposito != DEPOSITO_FORNECEDOR:
            continue

        # Garantir conversão numérica
        quantidade = float(str(quantidade).replace(",", "."))

        estoque[codigo] = quantidade

    print(
        f"✅ Estoque filtrado apenas para o depósito "
        f"{DEPOSITO_FORNECEDOR}"
    )
    print(f"📦 Total de SKUs considerados: {len(estoque)}")

    return estoque
