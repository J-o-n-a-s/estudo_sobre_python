def aumentar(valor: float, porcentagem: float) -> float:
    return valor + valor * (porcentagem / 100)


def diminuir(valor: float, porcentagem: float) -> float:
    return valor - valor * (porcentagem / 100)


def dobro(valor: float) -> float:
    return valor * 2


def metade(valor: float) -> float:
    return valor / 2


def moeda(valor: float) -> str:
    return f'R$ {valor:.2f}'.replace('.', ',')
