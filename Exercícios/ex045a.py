'''
Crie um programa que faça o computador jogar JOKENPÔ com você.
'''

from random import randint
from time import sleep

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
print('=' * 55)
print('VAMOS JOGAR JOKENPÔ?\n\nAs regras são:')
print(f'Selecione "{opcoes[0]}", "{opcoes[1]}" ou "{opcoes[2]}".')
print(f' > "{opcoes[0]}" ganha da "{opcoes[2]}".')
print(f' > "{opcoes[2]}" ganha do "{opcoes[1]}".')
print(f' > "{opcoes[1]}" ganha da "{opcoes[0]}".')
print('=' * 55 + '\n')

computador = randint(1, 3)
selecionado = int(input(f'Pressione:\n > 1 para "{opcoes[0]}";\n > 2 para "{opcoes[1]}";\n > 3 para "{opcoes[2]}".\n> '))

if not (selecionado == 1 or selecionado == 2 or selecionado == 3):
    print('Você selecionou uma opção inválida.')
else:
    print('JO')
    sleep(0.8)
    print('KEN')
    sleep(0.8)
    print('PÔ!!!')
    sleep(0.6)
    if computador == selecionado:
        print('NÓS EMPATAMOS! Ninguém ganhou!')
    elif computador == 1 and selecionado == 3 or computador == 2 and selecionado == 1 or computador == 3 and selecionado == 2:
        print('INFELIZMENTE, VOCÊ PERDEU!')
    elif selecionado == 1 and computador == 3 or selecionado == 2 and computador == 1 or selecionado == 3 and computador == 2:
        print('PARABÉNS! VOCÊ GANHOU!')
    print(f'Eu joguei "{opcoes[computador - 1]}"" e você jogou "{opcoes[selecionado - 1]}".')
print('\n' + '=' * 55 + '\n')