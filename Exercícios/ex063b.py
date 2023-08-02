'''
Crie um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

Exemplo:

0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

elementos = int(input('Quantos elementos de Fibonacci deseja visualizar: '))
copia_elementos = elementos
primeiro_termo = 0
segundo_termo = 1

print('')

while copia_elementos > 0:
    print(f'{primeiro_termo}{"" if copia_elementos == 1 else " ->"} ', end='')
    terceiro_termo = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    copia_elementos -= 1
print(f'\n\nOs {elementos} primeiros elementos da Sequência de Fibonacci foram apresentados acima.')
