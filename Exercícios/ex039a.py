'''
Crie um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

Se ele ainda vai se alistar ao serviço militar;
Se é a hora de se alistar;
Se já passou do tempo de alistamento. O programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date


ano_nascimento = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f'Você tem {idade} anos e ainda não precisa se alistar.')
elif idade == 18:
   print(f'Você tem {idade} anos e deve se alistar.')
elif idade > 18:
    print(f'Você tem {idade} anos e já passou do prazo de se alistar.')