'''
Crie um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

from time import sleep


contador = 0
numero = int(input('Digite um número: '))
divisores = []

print(f'\nAnalizando o número {numero}...\n')

for contagem in range(1, numero + 1):
    if numero % contagem == 0:
        contador += 1
        divisores.append(contagem)

if numero < 1000000:
    sleep(1.5)

if contador == 2:
    print(f'O número {numero} É PRIMO.')
else:
    print(f'O número {numero} NÃO É PRIMO.')

print(f'\nEle é divisível por {contador} número sendo:\n{divisores}.')