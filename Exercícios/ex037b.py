'''
Crie um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

1 para binário;
2 para octal;
3 para hexadecimal.
'''

from time import sleep


numero = int(input('Digite um número inteiro: '))
base = int(input('Selecione em qual base deseja visualizar o número:\n1 - Binário;\n2 - Octal;\n3 - Hexadecimal.\n> '))
bases = ['binária', 'octal', 'hexadecimal']

if base == 1:
    numero_convertido = bin(numero)[2:]
elif base == 2:
    numero_convertido = oct(numero)[2:]
elif base == 3:
    numero_convertido = '"' + hex(numero)[2:].upper() + '"'
else:
    print('Opção selecionada é inválida.')
    
print(f'Base "{bases[base - 1]}" selecionada. Processando...')
sleep(1.5)
print(f'O valor decimal {numero} convertido para base {bases[base - 1]} é {numero_convertido}.')