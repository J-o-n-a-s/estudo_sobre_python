'''
Crie um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

numero_01 = float(input('Digite o primeiro número: '))
numero_02 = float(input('Digite o segundo número: '))
numero_03 = float(input('Digite o terceiro número: '))
numeros = [numero_01, numero_02, numero_03]
maior_numero = max(numeros)
menor_numero = min(numeros)
print(f'O menor número é {menor_numero} e o maior número é {maior_numero}.')
