from utilidadesCeV import dado


def moeda(valor: float) -> str:
    return f'R$ {valor:.2f}'.replace('.', ',')


def resumo(valor: float, porcentagem_aumentar:float, porcentagem_diminuir:float) -> None:
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado:   {moeda(valor)}')
    print(f'Dobro do preço:    {dado.dobro(valor, True)}')
    print(f'Metade do preço:   {dado.metade(valor, True)}')
    print(f'{porcentagem_aumentar}% de aumento:    {dado.aumentar(valor, porcentagem_aumentar, True)}')
    print(f'{porcentagem_aumentar}% de redução:    {dado.diminuir(valor, porcentagem_diminuir, True)}')
    print('-' * 30)
