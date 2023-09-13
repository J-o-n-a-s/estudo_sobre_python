'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
 - O nome com todas as letras maiúsculas;
 - O nome com todas as letras minúsculas;
 - Quantas letras têm ao todo;
 - Quantas letras têm sem considerar espaços;
 - Quantas letras têm o primeiro nome.
'''

nome = input('Digite o seu nome completo: ').strip()
print('Analisando o seu nome...')
print(f'O nome completo em letra maiúscula é {nome.upper()}.')
print(f'O nome completo em letra minúscula é {nome.lower()}.')
print(f'O número total de letras do nome completo é {len(nome)}.')
tamanho = len(nome.replace(' ', ''))
print(f'O número total de letras do nome completo sem espaços é {tamanho}.')
print(f'O seu primeiro nome têm {nome.find(' ')} letras.')
