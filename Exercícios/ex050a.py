'''
Crie um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
Adicional: Deixe uma opção para o usuário escolher se deseja a soma de todos ímpares ou pares.
'''

inicio = 0
fim = 6
todos_valores = []
contador = 0
soma = 0

for contagem in range(inicio, fim):
    todos_valores.append(int(input('Digite um número inteiro: ')))
            
for contagem in range(inicio, fim):
    if todos_valores[contagem] % 2 == 0:
        contador += 1
        soma += todos_valores[contagem]

if contato == 1:
    print(f'\nFoi informado {contador} número "PAR" e a soma desse valor é {soma}.')
else:
    print(f'\nForam informados {contador} números "PARES" e a soma desses valores é {soma}.')