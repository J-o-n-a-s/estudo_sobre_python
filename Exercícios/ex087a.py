'''
Aprimore o exercício 087, mostrando no final:

A soma de todos os valores pares digitados;
A soma dos valores da terceira coluna;
O maior valor da segunda linha.
'''

valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_valores = []
soma_coluna = [0]
maior_valor_linha = [0]

for linha in range(0, 3):
    for coluna in range(0, 3):
        valores[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))

print('\n' + '-=' * 30 + '-')

for linha in range(0, 3):
    if linha == 1:
        maior_valor_linha[0] = max(valores[linha])  # Maior valor da segunda linha

    for coluna in range(0, 3):
        valor = valores[linha][coluna]
        
        print(f'[ {valor:^5} ]', end='')
        
        if valor % 2 == 0:
            soma_valores.append(valor)  # Pares
        if coluna == 2:
            soma_coluna[0] += valor  # Soma dos valores da terceira coluna

    print('')

print('-=' * 30 + '-')
soma = 0
for valor in soma_valores:
    soma += valor
print(f'A soma de todos os valores pares digitados é {soma}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna[0]}.')
print(f'O maior valor da segunda linha é {maior_valor_linha[0]}.')
