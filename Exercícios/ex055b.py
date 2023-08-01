'''
Crie um programa que leia o peso de cinco pessoas. No final, mostre qual foi o menor e o maior peso lidos.
'''

menor_peso = 0
maior_peso = 0

for contagem in range(0, 5):
    peso = float(input(f'Digite o peso da {contagem + 1}ª pessoa em kg: '))
    
    if contagem == 0:
        menor_peso = peso
        maior_peso = peso
    else:
        if menor_peso > peso:
            menor_peso = peso
    
        if maior_peso < peso:
            maior_peso = peso
        
print(f'O menor peso foi {menor_peso:.1f} kg e o maior peso foi {maior_peso:.1f} kg.')
