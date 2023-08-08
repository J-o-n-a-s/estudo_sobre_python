'''
Crie um programa que leia 5 valores númericos e guarde em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e o suas respectivas posições na lista.
'''

numero = []

for valor in range(0, 5):
    numero.append(int(input(f'Digite um número para a posição {valor}: ')))

print('-=' * 30 + '-')
print(f'Você digitou os números {numero}.')

menor_numero = min(numero)

print(f'O menor valor digitado foi {menor_numero} nas posições ', end='')

for valor in range(0, 5):
    if numero[valor] == menor_numero:
        print(f'-> {valor}', end='')

maior_numero = max(numero)
print('')
print(f'O maior valor digitado foi {maior_numero} nas posições ', end='')

for valor in range(0, 5):
    if numero[valor] == maior_numero:
        print(f'-> {valor}', end='')
