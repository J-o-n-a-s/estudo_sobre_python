'''
Melhore o jogo do exercício 028 onde o computador vai "pensar" em número entre 0 e 10. Só que agora, o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
from time import sleep


numero = randint(0, 10)
contador = 1
print('Vou pensar em um número entre 0 e 10. Tenta adivinhar o número que pensei.\n')

palpite = int(input('Qual número você acha que pensei: '))
print('Processando...')
sleep(1)

while palpite != numero:
    palpite = int(input('Desculpe, você errou. Tente novamente.\nQual número você acha que pensei: '))
    contador += 1
    print('Processando...')
    sleep(1)

print(f'O número que pensei foi {numero}.')
print(f'Parabéns! Você acertou no seu {contador}º palpite!')
