dias = int(input('Quantos dias alugou o carro? '))
quilometros = int(input('Quantos quilometros foram rodados? '))
print(f'O total a pagar pela locação do veículo é R$ {((dias * 60) + (quilometros * 0.15)):.2f}.')