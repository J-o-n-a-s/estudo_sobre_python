'''
Crie um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

numero_01 = float(input('Digite o primeiro número: '))
numero_02 = float(input('Digite o segundo número: '))
numero_03 = float(input('Digite o terceiro número: '))
maior_numero = numero_01
if numero_02 > numero_01 and numero_02 > numero_03:
    maior_numero = numero_02
if numero_03 > numero_01 and numero_03 > numero_02:
    maior_numero = numero_03
menor_numero = numero_01
if numero_02 < numero_01 and numero_02 < numero_03:
    menor_numero = numero_02
if numero_03 < numero_01 and numero_03 < numero_02:
    menor_numero = numero_03
print(f'O menor número é {menor_numero} e o maior número é {maior_numero}.')
