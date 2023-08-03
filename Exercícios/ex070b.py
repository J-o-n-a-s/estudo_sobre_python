'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

Qual é o total gasto na compra;
Quantos produtos custam mais de R$ 1.000,00;
Qual é o nome do produto mais barato.
'''

texto = ' LOJA SUPER BARATÃO'
total = 0
contador = 0
mais_de_mil = 0
produto_mais_barato = ''
preco_produto_mais_barato = 0

print('-' * 55)
print(f'{texto:^55}')
print('-' * 55)

while True:
    produto = input('Nome do produto: ').strip()
    preco = float(input('Preço do produto: R$ '))
    contador += 1
    total += preco
    
    if preco > 1000:
        mais_de_mil += 1
    
    if contador == 1 or preco_produto_mais_barato > preco:
        produto_mais_barato = produto
        preco_produto_mais_barato = preco

    continuar = ' '
            
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    
    if continuar == 'N':
        break

print('-' * 55, '\n')
print(f'O total da compra foi R$ {total:.2f}.')
print(f'Temos {mais_de_mil} produtos que custam mais de R$ 1.000,00.')
print(f'O produto mais barato foi {produto_mais_barato} que custou R$ {preco_produto_mais_barato:.2f}.')

texto = ' FIM DO PROGRAMA '
print(f'\n{texto:-^55}')
