from math import cos, radians, sin, tan
angulo = float(input('Digite o ângulo que deseja: '))
print(f'O ângulo de {angulo:.2f} tem o cosseno {cos(radians(angulo)):.2f}.')
print(f'O ângulo de {angulo:.2f} tem o seno {sin(radians(angulo)):.2f}.')
print(f'O ângulo de {angulo:.2f} tem a tangente {tan(radians(angulo)):.2f}.')