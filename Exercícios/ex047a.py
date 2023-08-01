'''
Crie um programa que mostre mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

from time import sleep

inicio = 1
fim = 50

for contagem in range(inicio, fim + 1):
    texto = ''
    if contagem % 2 == 0:
        if contagem < fim - 1:
            texto = ','
        print(f'{contagem}{texto}', end=' ')
        sleep(0.2)