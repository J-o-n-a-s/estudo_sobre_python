from random import randint
numero = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tenta adivinhar o número que pensei.')
chute = int(input('Qual número você acha que pensei: '))
if chute == numero:
    print('Parabéns! Você acertou!')
else:
    print('Desculpe, você perdeu!')
print(f'O número que pensei foi {numero}.')