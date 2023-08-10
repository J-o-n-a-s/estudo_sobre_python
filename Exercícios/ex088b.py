'''
Crie um programa que ajude um jogador da Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. Observações:

Não podem ter números repetido dentro do mesmo jogo;
Os jogos devem ser apresentados com os números em ordem crescente;
Adicionar um delay para apresentar cada um dos jogos.
'''

from random import randint
from time import sleep

jogos = []
numeros_sorteados = []
print('-' * 61 + f'\n{"JOGA NA MEGA SENA":^61}\n' + '-' * 61)
numero_jogos = int(input('Digite o número de jogos que deseja sortear: '))

for jogo in range(0, numero_jogos):
    while len(numeros_sorteados) < 6:
        numero_sorteado = randint(1, 60)
        if numero_sorteado not in numeros_sorteados:
            numeros_sorteados.append(numero_sorteado)
    
    numeros_sorteados.sort()
    jogos.append(numeros_sorteados[:])
    numeros_sorteados.clear()

print('-=' * 30 + '-' + f'\n{"SORTEANDO OS JOGOS":^61}\n' + '-=' * 30 + '-')

for numero, jogo in enumerate(jogos):
    sleep(0.7)
    print(f'Jogo {numero + 1}: {jogo}.')

print('-=' * 30 + '-' + f'\n{" > BOA SORTE! < ":^61}\n' + '-=' * 30 + '-')
