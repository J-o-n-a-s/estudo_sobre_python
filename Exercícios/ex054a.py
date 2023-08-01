'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade (21 anos) e quantas já são maiores.
'''

from datetime import date

ano_atual = date.today().year
menores_idade = 0
maiores_idade = 0

for contagem in range(0, 7):
    ano = int(input(f'Digite o ano de nascimento da {contagem + 1}ª pessoa: '))
    idade = ano_atual - ano
    
    if idade < 21:
        menores_idade += 1
    else:
        maiores_idade += 1
        
print(f'O número de pessoas menores de idade é {menores_idade}.')
print(f'O número de pessoas maiores de idade é {maiores_idade}.')
