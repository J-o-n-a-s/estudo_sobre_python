'''
Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA - Progressão Aritmética, mostrando os 10 primeiros termos da PA usando a estrutura "while".
'''

contador = 1
primeiro_termo = int(input('Digite o primeiro termo para realizar uma progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))

print(primeiro_termo, end='')
while contador < 10:
    print(f' -> {primeiro_termo + razao * contador}', end='')
    contador += 1
