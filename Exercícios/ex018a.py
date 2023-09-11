'''
Crie um programa que leia um ângulo qualquer e mostre na tela o valor do cosseno, seno e tangente desse ângulo.
'''

import math
angulo = float(input('Digite o ângulo que deseja: '))
print(f'O ângulo de {angulo:.2f} tem o cosseno {math.cos(math.radians(angulo)):.2f}.')
print(f'O ângulo de {angulo:.2f} tem o seno {math.sin(math.radians(angulo)):.2f}.')
print(f'O ângulo de {angulo:.2f} tem a tangente {math.tan(math.radians(angulo)):.2f}.')
