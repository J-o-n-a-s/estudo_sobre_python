from utilidadesCeV import moeda


def aumentar(valor: float, porcentagem: float, formatar: bool = False):
    if formatar:
        return moeda.moeda(valor + valor * (porcentagem / 100))

    return valor + valor * (porcentagem / 100)


def diminuir(valor: float, porcentagem: float, formatar: bool = False):
    if formatar:
        return moeda.moeda(valor - valor * (porcentagem / 100))

    return valor - valor * (porcentagem / 100)


def dobro(valor: float, formatar: bool = False):
    if formatar:
        return moeda.moeda(valor * 2)

    return valor * 2


def metade(valor: float, formatar: bool = False):
    if formatar:
        return moeda.moeda(valor / 2)

    return valor / 2
