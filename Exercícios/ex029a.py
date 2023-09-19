'''
Crie um programa que leia a velocidade de m carro.
Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite de velocidade.
'''

limite = 80
valor_multa = 7.00
velocidade = float(input("Digite a velocidade atual do carro: "))
if velocidade > limite:
    print(
        f'''
        Você foi multado! Excedeu o limite de 80 km/h.
        O valor da multa é R$ {((velocidade - limite) * valor_multa):.2f}.'''
    )
else:
    print('Continue dirigindo com segurança.')
