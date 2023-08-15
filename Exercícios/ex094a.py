'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

- Quantas pessoas foram cadastradas;
- A média de idade do grupo;
- Uma lista com todas as mulheres;
- Uma lista com todas as pessoas com idade acima da média.
'''

pessoa = {}
pessoas = []
soma_idade = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = input('Digite o nome: ').strip()
    while True:
        pessoa['Sexo'] = input('Digite o sexo: [M/F] ').strip().upper()[0]
        
        if pessoa['Sexo'] in 'MF':
            break
        
        print('ERRO! Por favor, digite apenas M ou F.')
 
    pessoa['Idade'] = int(input('Digite a idade: (anos) '))
    soma_idade += pessoa['Idade']
    pessoas.append(pessoa.copy())
    
    while True:
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
        
        if continuar in 'SN':
            break
        
        print('ERRO! Por favor, digite apenas S ou N.')
        print('-=' * 50 + '-')

    if continuar == 'N':
        break

print('-=' * 50 + '-')
print(f'A) Ao todo tem(os) {len(pessoas)} pessoa(s) cadastrada(s).')
media = soma_idade / len(pessoas)
print(f'B) A média de idade é de {(media):.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')

for pessoa in pessoas:
    if pessoa['Sexo'] == 'F':
        print(f'-> {pessoa["Nome"]}', end='')
        
print('.\nD) Lista das pessoas que estão acima da média:')

for pessoa in pessoas:
    if pessoa['Idade'] >= media:
        print(f'    Nome = {pessoa["Nome"]}, sexo = {pessoa["Sexo"]}, idade = {pessoa["Idade"]}.')

print('\n>> ENCERRADO <<')
