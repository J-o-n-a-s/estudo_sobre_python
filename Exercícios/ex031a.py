'''
Crie um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e cobre R$ 0,45 para viagens mais longas.
'''

distancia = float(input('Digite a distância em km do seu destino final: '))
valor_km_normal = 0.50
valor_km_desconto = 0.45
if distancia <= 200:
    valor = distancia * valor_km_normal
else:
    valor = distancia * valor_km_desconto
print(f'A sua passagem custa R$ {(valor):.2f}')
