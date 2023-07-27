'''
Crie um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

O primeiro valor é maior;
O segundo valor é maior;
Não existe valor maior, os dois são iguais.
'''

numero_01 = float(input('Digite o primeiro número: '))
numero_02 = float(input('Digite o segundo número: '))

if numero_01 > numero_02:
    print(f'O primeiro número ({numero_01}) é maior que o segundo número ({numero_02}).')
elif numero_01 < numero_02:
    print(f'O primeiro número ({numero_01}) é menor que o segundo número ({numero_02}).')
else:
    print(f'O primeiro número ({numero_01}) é igual o segundo número ({numero_02}).')