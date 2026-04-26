import requests

URL_PROCORTEX = (
    "https://metabase.procortex.com.br/"
    "api/public/dashboard/2322a2eb-60b9-4e2c-b54e-63759c1d9418/"
    "dashcard/104/card/118/json"
)


def buscar_estoque_procortex() -> dict:
    """
    Busca o estoque do fornecedor (Rio Preto) diretamente do Metabase
    Retorna um dicionário no formato: { sku: quantidade }
    """

    print("🔄 Buscando estoque online do Procortex (Rio Preto)...")

    response = requests.get(URL_PROCORTEX, timeout=30)

    if response.status_code != 200:
        raise Exception(
            f"Erro ao acessar Procortex: "
            f"{response.status_code} - {response.text}"
        )

    dados = response.json()
    estoque = {}

    for item in dados:
        sku = str(item.get("COD FABRICA", "")).strip()
        qtd_raw = str(item.get("ESTOQUE DISPONIVEL", "0")).strip()

        if not sku:
            continue

        # Normalização segura:
        # "1,060" -> 1060
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

    print(f"✅ Total de SKUs lidos: {len(estoque)}")

    return estoque
