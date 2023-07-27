'''
Crie um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

1 para binário;
2 para octal;
3 para hexadecimal.
'''

from time import sleep


numero = int(input('Digite um número inteiro: '))
base = int(input('Selecione em qual base deseja visualizar o número:\n1 - Binário;\n2 - Octal;\n3 - Hexadecimal.\n> '))

if base == 1:
    print('Base "binária" selecionada. Processando...')
    sleep(1.5)
    print(f'O valor decimal {numero} convertido para binário é {bin(numero)[2:]}.')
elif base == 2:
    print('Base "octal" selecionada. Processando...')
    sleep(1.5)
    print(f'O valor decimal {numero} convertido para octal é {oct(numero)[2:]}.')
elif base == 3:
    print('Base "hexadecimal" selecionada. Processando...')
    sleep(1.5)
    print(f'O valor decimal {numero} convertido para hexadecimal é "{hex(numero)[2:].upper()}".')
else:
    print('Opção selecionada é inválida.')