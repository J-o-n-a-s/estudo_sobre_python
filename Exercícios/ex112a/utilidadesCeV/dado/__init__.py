def leiaDinheiro(texto: str) -> float:
    while True:
        preco = input(texto).strip().replace(',', '.')

        if not preco.isalpha() and not preco == '':
            if 0 <= preco.count('.') <= 1:
                break

        print(f'ERRO: "{preco}" é um preço inválido!')

    return float(preco)
