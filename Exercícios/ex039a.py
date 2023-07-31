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

print(f'Quem nasceu em {ano_nascimento} têm {idade} anos em {ano_atual}.\n')

if idade < 18:
    print(f'Você ainda não precisa se alistar, falta(m) {18 - idade} ano(s).')
    print(f'Seu alistamento será em {ano_nascimento + 18}.')
elif idade == 18:
   print(f'Você completa ou completou {idade} anos este ano e deve se alistar.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} ano(s).')
    print(f'Seu alistamento deveria ter sido no ano de {ano_nascimento + 18}.')
