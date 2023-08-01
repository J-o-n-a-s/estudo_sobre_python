'''
Crie um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
Adicional: Deixe uma opção para o usuário escolher se deseja a soma de todos ímpares ou pares.
'''

from random import randint


inicio = 0
fim = 6
random_minimo = 1
random_maximo = 999
todos_valores = []
valores_pares = []
valores_impares = []
contador = 0
soma = 0

selecionado = int(input('Digite 1 se prefere números randomicos, ou digite 2 para digitar os seis valores:\n > '))
pares_impares = int(input('Digite 1 se deseja números pares, ou digite 2 se deseja números ímpares: '))

if selecionado in (1, 2) and pares_impares in (1, 2):
    for contagem in range(inicio, fim):
        if selecionado == 1:
            todos_valores.append(randint(random_minimo, random_maximo))
        else:
            todos_valores.append(int(input('Digite um número inteiro: ')))
            
    for contagem in range(inicio, fim):
        if todos_valores[contagem] % 2 == 0:
            valores_pares.append(todos_valores[contagem])
            
        if todos_valores[contagem] % 2 == 1:
            valores_impares.append(todos_valores[contagem])
            
    if pares_impares == 1:
        for contagem in range(0, len(valores_pares)):
            contador += 1
            soma += valores_pares[contagem]
    else:
        for contagem in range(0, len(valores_impares)):
            contador += 1
            soma += valores_impares[contagem]
    
    print('\nOs seis valores selecionados são:')
    print(f' - Ímpares {valores_impares}.')
    print(f' - Pares {valores_pares}.')
    if contador == 1:
        print(f'\nFoi informado {contador} número {"PAR" if pares_impares == 1 else "ÍMPAR"} e a soma desse valor é {soma}.')
    else:
        print(f'\nForam informados {contador} números {"PARES" if pares_impares == 1 else "ÍMPARES"} e a soma desses valores é {soma}.')
    
else:
    print(f'Você digitou uma opção inválida "{selecionado}". Tente novamente.')