'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
'''

import math
numero = input('Digite um número: ')
print(f'O valor digitado foi {numero} e a sua porção inteira é {math.trunc(float(numero))}.')
