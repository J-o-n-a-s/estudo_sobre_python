'''
Crie um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor_casa = float(input('Informe o valor da casa que deseja comprar: R$ '))
salario = float(input('Informe o valor do seu salário mensal: R$ '))
tempo = int(input('Informe o número de parcelas que deseja pagar: '))
valor_parcelas = valor_casa / tempo
print(f'O valor da prestação mensal é R$ {valor_parcelas:.2f}.')
if (salario * 0.3) > valor_parcelas:
    print('Parabéns! O seu financiamento foi aprovado.')
else:
    print('Infelizmento o seu financiamento foi reprovado, pois excede 30% do seu salário.')
print(
    f'O seu salário é R$ {salario:.2f}. O valor das parcelas é R$ {valor_parcelas:.2f}.\n'
    f'As parcelas compromentem {(valor_parcelas * 100 / salario):.2f}% do seu salário.'
)