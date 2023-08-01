'''
Crie um programa que leia o primeiro termo e a ração de uma PA - Progressão Aritmética.
No final, mostre os 10 primeiros termos dessa progressão.
'''

primeiro_termo = int(input('Digite o primeiro termo para realizar uma progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))

print(primeiro_termo, end='')
for contagem in range(primeiro_termo + razao, primeiro_termo + razao * 10, razao):
    print(f' - {contagem}', end='')