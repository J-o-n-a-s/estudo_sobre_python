'''
Crie um programa que leia o nome completo de uma pessoa e informe se tem "SILVA" no nome.
'''

nome = input('Digite o seu nome completo: ').strip()
resultado = 'SILVA' in nome.upper()
print(f'O seu nome contém "SILVA"?\n{resultado}.')
