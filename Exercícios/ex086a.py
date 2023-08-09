'''
Crie um programa que crie uma matriz de dimensões 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''

valores = [[], [], []]

for valor in range(0, 9):
    numero = int(input(f'Digite o {valor + 1}º número inteiro: '))
    valores[valor // 3].append(numero)

for lista in valores:
    print('')
    for numero in lista:
        print(f'[ {numero:^5} ]', end='')
