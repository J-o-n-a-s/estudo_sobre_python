'''
Crie um programa que tenha uma função chamada área(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def linha(caracter: str, texto: str):
    print(caracter * len(texto))


def titulo(texto: str):
    texto = ' ' + texto + ' '
    linha('-', texto)
    print(texto)
    linha('-', texto)


def area(p_largura: float, p_comprimento: float):
    print(f'A área de um terreno de {p_largura} x {p_comprimento} m é {p_largura * p_comprimento} m².')


titulo(' Controle de terrenos ')

largura = float(input('Largura (m):'))
comprimento = float(input('Comprimento (m):'))

area(largura, comprimento)
