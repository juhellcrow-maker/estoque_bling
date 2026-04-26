import json


def buscar_estoque_procortex(caminho_arquivo: str) -> dict:
    """
    Lê o arquivo JSON do Procortex (Rio Preto)
    e retorna um dicionário {sku: quantidade}
    """

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)

    estoque = {}

    for item in dados:
        sku = str(item.get("COD FABRICA", "")).strip()
        qtd_raw = str(item.get("ESTOQUE DISPONIVEL", "0")).strip()

        if not sku:
            continue

        # Normaliza quantidade (1.060 / 1,060 / 1060)
        qtd_normalizada = (
            qtd_raw
            .replace(".", "")
            .replace(",", ".")
        )

        try:
            quantidade = int(float(qtd_normalizada))
        except ValueError:
            quantidade = 0

        estoque[sku] = quantidade

    return estoque
