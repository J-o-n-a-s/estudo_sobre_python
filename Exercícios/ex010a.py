'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere o valor de um dólar = R$ 4,73 (Data: 24/07/2023)
'''

cotacao = float(input('Quanto dinheiro você tem agora na carteira? R$ '))
print(f'Com {cotacao:.2f} reais você consegue comprar {(cotacao / 4.73):.2f} dólares.')
