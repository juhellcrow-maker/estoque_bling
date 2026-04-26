# estoque_calc.py

def calcular_comprometido(pedidos, sku):
    comprometido = 0

    for pedido in pedidos:
        for item in pedido["itens"]:
            if item["codigo"] == sku:
                comprometido += item["quantidade"]

    return comprometido


def calcular_disponivel(estoque_fornecedor, comprometido):
    if comprometido > estoque_fornecedor:
        raise ValueError(
            f"Comprometido ({comprometido}) maior que fornecedor ({estoque_fornecedor})"
        )

    return estoque_fornecedor - comprometido
