'''
Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura}x{altura}m e sua área é {area}m².')
print(f'Para pintar essa parede, você precisa de {area / 2}l de tinta.')
