'''
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final mostre os valores pares e ímpares em ordem crescente.
'''

valores = [[], []]

for valor in range(1, 8):
    numero = int(input(f'Digite o {valor}º número inteiro: '))
    valores[numero % 2].append(numero)

valores[0].sort()
valores[1].sort()

print('\n' + '-=' * 30 + '-')

if len(valores[0]) > 0:
	print(f'Dentre os valores digitados os pares são {valores[0]}.')

if len(valores[1]) > 0:
	print(f'Dentre os valores digitados os ímpares são {valores[1]}.')
