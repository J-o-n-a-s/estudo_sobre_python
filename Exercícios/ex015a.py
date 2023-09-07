'''
Crie um programa que leia a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0.15 por quilômetro rodado.
'''

dias = int(input('Quantos dias alugou o carro? '))
quilometros = float(input('Quantos quilometros foram rodados? '))
print(f'O total a pagar pela locação do veículo é R$ {((dias * 60) + (quilometros * 0.15)):.2f}.')
