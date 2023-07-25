import math
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.sqrt((math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2)))
print(f'Um triângulo retângulo com cateto oposto {cateto_oposto} e cateto adjacente {cateto_adjacente} tem hipotenusa {hipotenusa:.2f}.')