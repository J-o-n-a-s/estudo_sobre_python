def aumentar(valor: float, porcentagem: float, formatar: bool = False):
    if formatar:
        return moeda(valor + valor * (porcentagem / 100))

    return valor + valor * (porcentagem / 100)


def diminuir(valor: float, porcentagem: float, formatar: bool = False):
    if formatar:
        return moeda(valor - valor * (porcentagem / 100))

    return valor - valor * (porcentagem / 100)


def dobro(valor: float, formatar: bool = False):
    if formatar:
        return moeda(valor * 2)

    return valor * 2


def metade(valor: float, formatar: bool = False):
    if formatar:
        return moeda(valor / 2)

    return valor / 2


def moeda(valor: float) -> str:
    return f'R$ {valor:.2f}'.replace('.', ',')


def resumo(valor: float, porcentagem_aumentar:float, porcentagem_diminuir:float) -> None:
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado:   {moeda(valor)}')
    print(f'Dobro do preço:    {dobro(valor, True)}')
    print(f'Metade do preço:   {metade(valor, True)}')
    print(f'{porcentagem_aumentar}% de aumento:    {aumentar(valor, porcentagem_aumentar, True)}')
    print(f'{porcentagem_aumentar}% de redução:    {diminuir(valor, porcentagem_diminuir, True)}')
    print('-' * 30)
