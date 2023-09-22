'''
Crie um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

numero_01 = float(input('Digite o primeiro número: '))
numero_02 = float(input('Digite o segundo número: '))
numero_03 = float(input('Digite o terceiro número: '))
if numero_01 > numero_02:
    if numero_01 > numero_03:
        maior_numero = numero_01
    else:
        maior_numero = numero_03
    if numero_02 < numero_03:
        menor_numero = numero_02
    else:
        menor_numero = numero_03
else:
    if numero_02 > numero_03:
        maior_numero = numero_02
    else:
        maior_numero = numero_03
    if numero_01 < numero_03:
        menor_numero = numero_01
    else:
        menor_numero = numero_03
print(f'O menor número é {menor_numero} e o maior número é {maior_numero}.')
