'''
Crie um programa que leia um número qualquer e mostre o seu fatorial (usando "for" e usando "while").

Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120.
'''

from math import factorial


print('-' * 35, '\nCÁLCULO FATORIAL DE UM NÚMERO\n')

numero = int(input('Digite um número: '))
print(f'\nO resultado de {numero}! é {factorial(numero)}.')
print('-' * 35)
