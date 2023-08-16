'''
Crie um programa que tenha uma função maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

from random import randint
from time import sleep

def maior(numeros: list):
    sleep(1)
    print('Analisando os valores passados...')
    for numero in numeros:
        sleep(1)
        print(f'-> {numero} ', end='', flush=True)
    sleep(1)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {max(numeros)}.')
    
quantidade_vezes = randint(1, 4)
numeros = []

for contador01 in range(0, quantidade_vezes):
    print('-=' * 30 + '-')
    quantidade_numeros = randint(0, 6)
    numeros.clear()
    for contador02 in range(0, quantidade_numeros):
        numeros.append(randint(0, 9))
    maior(numeros)
