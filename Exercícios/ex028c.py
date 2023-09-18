'''
Crie um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep
numero = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tenta adivinhar o número que pensei.')
chute = int(input('Qual número você acha que pensei: '))
print('Processando...')
sleep(2)
if chute == numero:
    print('Parabéns! Você acertou!')
else:
    print('Desculpe, você perdeu!')
print(f'O número que pensei foi {numero}.')
