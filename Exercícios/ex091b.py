'''
Crie um programa onde 4 jogadores joguem um dado (entre 1 e 6) e tenha resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

resultados = {}
ranking = []

print('-=' * 30 + '-' + '\nValores sorteados:')

for contador in range(1, 5):
    chave = f'Jogador 0{contador}'
    resultados[chave] = randint(1, 6)
    print(f'{chave} tirou {resultados[chave]} no dado.')
    sleep(1.5)

print('-=' * 30 + '-')
sleep(0.8)
print(' ==== RANKING DOS JOGADORES ==== ')

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)

for numero, valor in enumerate(ranking):
    sleep(1.2)
    print(f'   {numero + 1}º lugar: {valor[0]} com {valor[1]}.')

sleep(1.2)

print('-=' * 30 + '-')

sleep(0.7)
