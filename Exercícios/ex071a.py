'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$ 50,00, R$ 20,00, R$ 10,00 e R$ 1,00.
'''

texto = ' BANCO DO JONAS '
cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
cedulas_1 = 0

print('=' * 50)
print(f'{texto:^50}')
print('=' * 50)

while True:
    valor = int(input('Digite o valor que deseja sacar: R$ '))
    cedulas_50 = valor // 50
    valor = valor % 50
    cedulas_20 = valor // 20
    valor = valor % 20
    cedulas_10 = valor // 10
    valor = valor % 10
    cedulas_1 = valor
    break
    
print(f'Total de {cedulas_50} cédulas de R$ 50,00.')
print(f'Total de {cedulas_20} cédulas de R$ 20,00.')
print(f'Total de {cedulas_10} cédulas de R$ 10,00.')
print(f'Total de {cedulas_1} cédulas de R$ 1,00.')
print('=' * 50)
print('Volte sempre ao Banco do Jonas!')
