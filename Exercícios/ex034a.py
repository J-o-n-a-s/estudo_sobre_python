'''
Crie um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento será de 15%.
'''

salario_base = 1250.00
salario = float(input('Digite o salário do funcionário: R$ '))
if salario > salario_base:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.15
print(f'O novo salário do funcionário é R$ {novo_salario:.2f}.')
