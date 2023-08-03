'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:

Quantas pessoas têm mais de 18 anos;
Quantos homens foram cadastrados;
Quantas mulheres têm menos de 20 anos.
'''

pessoas_mais_18 = 0
homens = 0
mulheres_menos_20 = 0
texto = 'CADASTRE UMA PESSOA'

print('=' * 10, 'INÍCIO DO PROGRAMA', '=' * 10)

while True:
    print('-' * 40)
    print(f'{texto:^40}')
    print('-' * 40)
    
    idade = int(input('Idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
        
    print('-' * 40)
    
    if idade >= 18:
        pessoas_mais_18 += 1
    
    if sexo == 'M':
        homens += 1
    
    if idade < 20 and sexo == 'F':
        mulheres_menos_20 += 1

    continuar = ' '    

    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    
    if continuar == 'N':
        break

print('-' * 40, '\n')
print(f'Total de pessoas com mais de 18 anos: {pessoas_mais_18}.')

if homens == 1:
    texto = f'Teve {homens} homem cadastrado.'
else:
    texto = f'Tiveram {homens} homens cadastrados.'
    
print(texto)

if mulheres_menos_20 == 1:
    texto = f'E temos {mulheres_menos_20} mulher com menos de 20 anos.'
else:
    texto = f'E temos {mulheres_menos_20} mulheres com menos de 20 anos.'
    
print(texto)
print('\n', '=' * 10, 'FINAL DO PROGRAMA', '=' * 11)
