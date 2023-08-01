'''
Crie um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:

A média de idade do grupo;
Qual é o nome do homem mais velho;
Quantas mulheres têm menos de 20 anos.
'''

soma_idade = 0
nome_mais_velho = ''
idade_mais_velho = 0
mulheres_menos_20_anos = 0

for contagem in range(0, 4):
    print('-' * 6, f"{contagem + 1}ª PESSOA", '-' * 6)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').upper().strip()
    
    soma_idade += idade
    
    if idade_mais_velho < idade and sexo == 'M':
        nome_mais_velho = nome
        idade_mais_velho = idade
    
    if idade < 20 and sexo == 'F':
        mulheres_menos_20_anos += 1

print('-' * 23)
print(f'\nO média de idade do grupo é {(soma_idade / 4):.1f} anos.')
print(f'O homem mais velho é o {nome_mais_velho} e ele tem {idade_mais_velho} anos.')
print(f'O grupo têm {mulheres_menos_20_anos} mulher(es) com menos de 20 anos.')
