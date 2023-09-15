'''
Crie um programa que leia o nome completo de uma pessoa, mostrando o primeiro e o último nome separadamente.
 - Exemplo "Ana Maria da Silva":
   - Primeiro = Ana
   - Último = Silva
'''

nome = input('Digite seu nome completo: ').strip()
nome_completo = nome.split()
print(f'Seu primeiro nome é {nome_completo[0]} e seu último nome é {nome_completo[-1]}.')
