'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
'''

from math import trunc
numero = input('Digite um número: ')
print(f'O valor digitado foi {numero} e a sua porção inteira é {trunc(float(numero))}.')
