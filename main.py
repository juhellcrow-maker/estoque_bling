from procortex import buscar_estoque_procortex

SKU_TESTE = "4504400"


def main():
    print("======================================")
    print("ETAPA 1 - Leitura ONLINE do Procortex")
    print("======================================")

    estoque = buscar_estoque_procortex()

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
