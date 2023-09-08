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
