'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

produtos_precos = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Tranferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

print('-' * 60)
print(f'{" LISTAGEM DE PREÇOS ":^60}')
print('-' * 60)

for contagem in range(0, len(produtos_precos)):
    if contagem % 2 == 0:
        print(f'{produtos_precos[contagem]:.<50}', end='')
    else:
        print(f'R${produtos_precos[contagem]:>7.2f}')

print('-' * 60)
