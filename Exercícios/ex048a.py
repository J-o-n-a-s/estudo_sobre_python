'''
Crie um programa que calcule a soma de todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

inicio = 1
fim = 500
contador = 0
soma = 0

for contagem in range(inicio, fim + 1):
    texto = ''
    if contagem % 3 == 0 and contagem % 2 == 1:
        if contagem < fim - 1:
            texto = ','
        contador += 1
        soma += contagem
        print(f'{contagem}{texto}', end=' ')
        # sleep(0.2)
print(f'\n\nA soma de todos os {contador} valores impares múltiplos de três é {soma}.')