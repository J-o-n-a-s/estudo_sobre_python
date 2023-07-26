reta_01 = float(input('Digite o tamanho da primeiro reta: '))
reta_02 = float(input('Digite o tamanho da segundo reta: '))
reta_03 = float(input('Digite o tamanho da terceiro reta: '))
resultado_01 = reta_01 < reta_02 + reta_03
resultado_02 = reta_02 < reta_01 + reta_03
resultado_03 = reta_03 < reta_01 + reta_02
possivel_triangulo = resultado_01 and resultado_02 and resultado_03
print(f'É possivel montar um triângulo com as medidas {reta_01}, {reta_02} e {reta_03}?\n{possivel_triangulo}')