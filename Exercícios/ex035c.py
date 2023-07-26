reta_01 = float(input('Digite o tamanho da primeiro reta: '))
reta_02 = float(input('Digite o tamanho da segundo reta: '))
reta_03 = float(input('Digite o tamanho da terceiro reta: '))
possivel_triangulo = reta_01 < reta_02 + reta_03 and reta_02 < reta_01 + reta_03 and reta_03 < reta_01 + reta_02
print(f'É possivel montar um triângulo com as medidas {reta_01}, {reta_02} e {reta_03}?\n{possivel_triangulo}')