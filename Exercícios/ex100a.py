'''
Crie um programa que tenha uma lista chamada números e duas funções sorteio() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''

from random import randint
from time import sleep


def sorteio(valores: list):
    print('-=' * 30 + '-')
    sleep(0.5)
    print('Sorteando 5 valores da lista:', end='')

    for contador in range(0, 5):
        sleep(0.5)
        valor = randint(0, 10)
        valores.append(valor)
        print(f' -> {valor}', end='', flush=True)
    
    print('.')
    

def somaPar(valores: list):
    soma_pares = 0
    for valor in valores:
        if valor % 2 == 0:
            soma_pares += valor
    
    print(f'Somando os valores pares de {valores}, temos {soma_pares}.')


numeros = []

sorteio(numeros)
somaPar(numeros)
