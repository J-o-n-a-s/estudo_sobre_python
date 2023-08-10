'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date

ano_atual = date.today().year

print('-=' * 30, '-')

trabalhador = {
    'Nome': input('Nome: ').strip(),
    'Idade': ano_atual - int(input('Ano de nascimento: ')),
    'CTPS': int(input('Carteira de trabalho (0 não tem): '))
}
if trabalhador['CTPS'] != 0:
    trabalhador['Ano de contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] - (ano_atual - trabalhador['Ano de contratação']) + 35

print('-=' * 30, '-')

for chave, valor in trabalhador.items():
    print(f'  - {chave} tem o valor {valor}.')
