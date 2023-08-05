'''
Crie um programa que vai gerar 5 números aleatórios e vai colocar numa tupla.
Depois disso, mostre a listagem de números gerados e também indique o menos e o maior valor que estão na tupla.
'''

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: {numeros}.')
print(f'O menor valor sorteado foi {sorted(numeros)[0]}.')
print(f'O maior valor sorteado foi {sorted(numeros)[-1]}.')
