'''
Crie um programa que leia a temperatura em graus Celsius e converta para uma temperatura em Fahrenheit.
'''

temperatura = float(input('Informe a temperatura em ºC: '))
print(f'A temperatura de {temperatura} ºC corresponde a {(temperatura * 9 / 5 + 32):.1f} ºF.')
