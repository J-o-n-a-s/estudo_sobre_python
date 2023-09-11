'''
Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto * cateto_oposto + cateto_adjacente * cateto_adjacente) ** 0.5
print(f'Um triângulo retângulo com cateto oposto {cateto_oposto} e cateto adjacente {cateto_adjacente} tem hipotenusa {hipotenusa:.2f}.')
