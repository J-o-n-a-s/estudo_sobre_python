'''
Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

Equilátero: Todos os lados iguais;
Isósceles: Dois lados iguais;
Escaleno: Todos os lados diferentes.
'''

reta_01 = float(input('Digite o tamanho da primeiro reta: '))
reta_02 = float(input('Digite o tamanho da segundo reta: '))
reta_03 = float(input('Digite o tamanho da terceiro reta: '))
possivel_triangulo = reta_01 < (reta_02 + reta_03) and reta_02 < (reta_01 + reta_03) and reta_03 < (reta_01 + reta_02)
print(f'É possivel montar um triângulo com as medidas {reta_01}, {reta_02} e {reta_03}?\n{possivel_triangulo}')

if possivel_triangulo:
    if reta_01 == reta_02 and reta_02 == reta_03:
        print('O triângulo tem todos os lados iguais, ou seja, ele é EQUILÁTERO.')
    elif reta_01 != reta_02 and reta_02 != reta_03 and reta_03 != reta_01:
        print('O triângulo tem todos os lados diferentes, ou seja, ele é ESCALENO.')
    elif (reta_01 == reta_02 and reta_02 != reta_03) or  (reta_01 == reta_03 and reta_02 != reta_03) or (reta_02 == reta_03 and reta_01 != reta_02):
        print('O triângulo tem doiS lados iguais, ou seja, ele é ISÓSCELES.')
    else:
        print('Essa mensagem nunca pode aparecer. Caso apareça, alguma coisa errada não está certa.')