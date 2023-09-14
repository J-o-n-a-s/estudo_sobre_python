'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO".
'''

nome = input('Digite o nome de uma cidade: ').strip()
resultado = nome[:5].upper() == 'SANTO'
print(f'O nome da cidade começa com "SANTO"?\n{resultado}.')
