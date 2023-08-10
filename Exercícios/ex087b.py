'''
Aprimore o exercício 087, mostrando no final:

A soma de todos os valores pares digitados;
A soma de todos os valores ímpares digitados;
A soma dos valores da primeira coluna;
A soma dos valores da segunda coluna;
A soma dos valores da terceira coluna;
A soma dos valores da primeira linha;
A soma dos valores da segunda linha;
A soma dos valores da terceira linha;
O menor e o maior valor de cada linha;
O menor e o maior valor de cada coluna;
O valor média da matriz;
O valor média de cada linha;
O valor média de cada coluna.
'''

valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_valores = [[], []]
soma_linha = [0, 0, 0]
soma_coluna = [0, 0, 0]
menor_valor_linha = [0, 0, 0]
maior_valor_linha = [0, 0, 0]
menor_valor_coluna = [0, 0, 0]
maior_valor_coluna = [0, 0, 0]
media_valor_linha = [0, 0, 0]
media_valor_coluna = [0, 0, 0]

for linha in range(0, 3):
    for coluna in range(0, 3):
        valores[linha][coluna] = int(input(f'Digite o valor para [{linha}, {coluna}]: '))

print('\n' + '-=' * 30 + '-')

for linha in range(0, 3):
    menor_valor_linha[linha] = min(valores[linha])  # Menor valor de cada linha
    maior_valor_linha[linha] = max(valores[linha])  # Maior valor de cada linha

    for coluna in range(0, 3):
        valor = valores[linha][coluna]
        
        print(f'[ {valor:^5} ]', end='')
        
        soma_valores[valor % 2].append(valor)  # Pares e ímpares
        soma_linha[linha] += valor  # Soma dos valores de cada linha
        soma_coluna[coluna] += valor  # Soma dos valores de cada coluna
        
        if linha == 0:
            menor_valor_coluna[coluna] = valor
            maior_valor_coluna[coluna] = valor
        else:
            if menor_valor_coluna[coluna] > valor:
                menor_valor_coluna[coluna] = valor
            
            if maior_valor_coluna[coluna] < valor:
                maior_valor_coluna[coluna] = valor
    
    print('')

print('-=' * 30 + '-')
soma = 0
for valor in soma_valores[0]:
    soma += valor
print(f'A soma de todos os valores pares digitados é {soma}.')
soma = 0
for valor in soma_valores[1]:
    soma += valor
print(f'A soma de todos os valores ímpares digitados é {soma}.')
print(f'A soma dos valores da primeira coluna é {soma_coluna[0]}.')
print(f'A soma dos valores da segunda coluna é {soma_coluna[1]}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna[2]}.')
print(f'A soma dos valores da primeira linha é {soma_linha[0]}.')
print(f'A soma dos valores da segunda linha é {soma_linha[1]}.')
print(f'A soma dos valores da terceira linha é {soma_linha[2]}.')
print(f'O menor valor da primeira linha é {menor_valor_linha[0]}.')
print(f'O menor valor da segunda linha é {menor_valor_linha[1]}.')
print(f'O menor valor da terceira linha é {menor_valor_linha[2]}.')
print(f'O maior valor da primeira linha é {maior_valor_linha[0]}.')
print(f'O maior valor da segunda linha é {maior_valor_linha[1]}.')
print(f'O maior valor da terceira linha é {maior_valor_linha[2]}.')
print(f'O menor valor da primeira coluna é {menor_valor_coluna[0]}.')
print(f'O menor valor da segunda coluna é {menor_valor_coluna[1]}.')
print(f'O menor valor da terceira coluna é {menor_valor_coluna[2]}.')
print(f'O maior valor da primeira coluna é {maior_valor_coluna[0]}.')
print(f'O maior valor da segunda coluna é {maior_valor_coluna[1]}.')
print(f'O maior valor da terceira coluna é {maior_valor_coluna[2]}.')
print(f'O valor média da matriz é {(soma_linha[0] + soma_linha[1] + soma_linha[2]) / 9:.1f}.')
print(f'O valor médio da primeira linha é {soma_linha[0] / 3:.1f}.')
print(f'O valor médio da segunda linha é {soma_linha[1] / 3:.1f}.')
print(f'O valor médio da terceira linha é {soma_linha[2] / 3:.1f}.')
print(f'O valor médio da primeira coluna é {soma_coluna[0] / 3:.1f}.')
print(f'O valor médio da segunda coluna é {soma_coluna[1] / 3:.1f}.')
print(f'O valor médio da terceira coluna é {soma_coluna[2] / 3:.1f}.')
