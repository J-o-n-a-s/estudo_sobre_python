'''
Crie um programa que crie uma matriz de dimensões 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''

valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        valores[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))

for linha in range(0, 3):
    print()
    for coluna in range(0, 3):
        print(f'[ {valores[linha][coluna]:^5} ]', end='')
