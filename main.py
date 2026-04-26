from procortex import buscar_estoque_procortex

SKU_TESTE = "4504400"
ARQUIVO_ESTOQUE = "estoque_rio_preto_2026-04-26T21_12_54.101357277Z.json"


def main():
    print("======================================")
    print("ETAPA 1 - Leitura do Procortex")
    print("======================================")

    estoque = buscar_estoque_procortex(ARQUIVO_ESTOQUE)

    if SKU_TESTE not in estoque:
        print(f"❌ SKU {SKU_TESTE} não encontrado")
        return

    print(f"✅ SKU {SKU_TESTE}")
    print(f"Fornecedor (Rio Preto): {estoque[SKU_TESTE]} unidades")

    print("======================================")
    print("ETAPA 1 FINALIZADA COM SUCESSO")
    print("======================================")


if __name__ == "__main__":
    main()
