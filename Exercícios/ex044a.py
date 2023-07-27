'''
Crie um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

À vista no dinheiro/cheque: 10% de desconto;
À vista no cartão de débito: 5% de desconto;
Em até 2x no cartão de crédito: Preço normal;
Em 3x ou mais no cartão de crédito: 20% de juros.
'''

valor_produto = float(input('Digite o valor do produto: R$ '))
formas = [
    '1 - À vista no dinheiro/cheque',
    '2 - À vista no cartão de débito',
    '3 - Em até 2x no cartão de crédito',
    '4 - Em 3x ou mais no cartão de crédito'
]

forma_pagamento = f'Selecione a forma de pagamento:\n{formas[0]};\n{formas[1]};\n{formas[2]};\n{formas[3]}.'

selecao_pagamento = int(input(forma_pagamento))
selecao_valida = True

if selecao_pagamento == 1:
    valor_pagar = valor_produto * 0.9
elif selecao_pagamento == 2:
    valor_pagar = valor_produto * 0.95
elif selecao_pagamento == 3:
    valor_pagar = valor_produto
elif selecao_pagamento == 4:
    valor_pagar = valor_produto * 1.2
else:
    selecao_valida = False
    
if selecao_valida:
    print(f'A forma de pagamento selecionada foi "{formas[selecao_pagamento - 1]}".\n O valor total a pagar é R$ {valor_pagar:.2f}')
else:
    print('Você selecionou uma seleção inválida. Tente novamente.')