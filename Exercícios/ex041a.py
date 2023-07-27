'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com idade:

Até 9 anos = MIRIM;
Até 14 anos = INFANTIL;
Até 19 anos = JÚNIOR;
Até 20 anos = SÊNIOR;
Acima = MASTER.
'''

from datetime import date


ano_atual = date.today().year
ano_nascimento = int(input('Informe o ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade < 0:
    print(f'O ano digitado ({ano_nascimento}) está incorreto. Favor verificar.')
else:
    print(f'A idade atual desse atleta é {idade} anos e sua categoria é', end=' ')
    
    if idade < 9:
        print('MIRIM.')
    elif idade >= 9 and idade <= 14:
        print('INFANTIL.')
    elif idade >= 14 and idade <= 19:
        print('JÚNIOR.')
    elif idade == 20:
        print('SÊNIOR.')
    elif idade > 20:
        print('MASTER.')