dias = int(input('Quantos dias alugou o carro? '))
quilometros = float(input('Quantos quilometros foram rodados? '))
print(f'O total a pagar pela locação do veículo é R$ {((dias * 60) + (quilometros * 0.15)):.2f}.')