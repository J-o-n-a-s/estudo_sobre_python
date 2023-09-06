'''
Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

medida = float(input('Digite uma medida em metros: '))
print(f'A medidade {medida}m corresponde a {(medida * 100):.0f}cm e {(medida * 1000):.0f}mm.')
