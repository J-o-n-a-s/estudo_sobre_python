'''
Crie um programa onde 4 jogadores joguem um dado (entre 1 e 6) e tenha resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep

resultados = {}

print('Valores sorteados:')

for contador in range(1, 5):
    chave = f'Jogador 0{contador}'
    resultados[chave] = randint(1, 6)
    sleep(1.5)
    
    print(f'{chave} tirou {resultados[chave]} no dado.')
    

copia_resultados = resultados.copy()
tamanho = len(copia_resultados)
resultados = {}

sleep(1.2)
print('-=' * 30 + '-')
sleep(0.8)
print(' ==== RANKING DOS JOGADORES ==== ')

for contador in range(0, tamanho):
    maior_valor = 0
    chave_maior_valor = ''
    
    for chave, valor in copia_resultados.items():
        if maior_valor < valor:
            maior_valor = valor
            chave_maior_valor = chave
            
    del copia_resultados[chave_maior_valor]
    resultados[chave_maior_valor] = maior_valor

contador = 1

for chave, valor in resultados.items():
    sleep(1.2)
    print(f'   {contador}º lugar: {chave} com {valor}.')
    contador += 1
    
sleep(1.2)
