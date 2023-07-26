distancia = float(input('Digite a distância em km do seu destino final: '))
valor_km_normal = 0.50
valor_km_desconto = 0.45
if distancia <= 200:
    valor = distancia * valor_km_normal
else:
    valor = distancia * valor_km_desconto
print(f'A sua passagem custa R$ {(valor):.2f}')