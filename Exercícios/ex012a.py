'''
Crie um programa que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.
'''

promocao = float(input('Digite o preço do produto para ver seu valor com 5% de desconto: R$'))
print(f'O valor do produto é R$ {promocao:.2f}. Na promoção o produto sai por R$ {(promocao * 0.95):.2f}.')
