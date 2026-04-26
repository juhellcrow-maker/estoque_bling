# main.py

from config import SKU_TESTE, DEPOSITO_ID, DEPOSITO_NOME, MODO_TESTE
from procortex import buscar_estoque_fornecedor
from bling import buscar_pedidos_nao_faturados
from estoque_calc import calcular_comprometido, calcular_disponivel
from logger import log


def main():
    log("======================================")
    log("Iniciando ETAPA 1 - Leitura e cálculo")
    log(f"SKU TESTE: {SKU_TESTE}")
    log(f"Depósito: {DEPOSITO_NOME} ({DEPOSITO_ID})")
    log("======================================")

    estoque_procortex = buscar_estoque_fornecedor()

    if SKU_TESTE not in estoque_procortex:
        log(f"❌ SKU {SKU_TESTE} não encontrado no fornecedor")
        return

    estoque_total = estoque_procortex[SKU_TESTE]
    log(f"Fornecedor (Procortex): {estoque_total}")

    pedidos = buscar_pedidos_nao_faturados()
    comprometido = calcular_comprometido(pedidos, SKU_TESTE)
    log(f"Comprometido no Bling: {comprometido}")

    estoque_disponivel = calcular_disponivel(estoque_total, comprometido)
    log(f"✅ Estoque disponível calculado: {estoque_disponivel}")

    log("======================================")
    log("ETAPA 1 FINALIZADA COM SUCESSO")
    log("Nenhuma atualização no Bling foi feita")
    log("======================================")


if __name__ == "__main__":
    main()
