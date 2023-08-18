'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
Obs.: Com 16, 17 e acima de 65 anos, o voto é OPCIONAL.
'''

from datetime import date


def voto(ano_nascimento: int) -> str:
    idade = ano_atual - ano_nascimento
    texto = f'Com {idade} anos: VOTO '

    if idade < 16:
        return texto + 'NEGADO'
    elif 18 <= idade < 65:
        return texto + 'OBRIGATÓRIO'
    else:
        return texto + 'OPCIONAL'


print('-' * 30)

ano_atual = date.today().year
nascimento = int(input('Em que ano você nasceu: '))
condicao = voto(nascimento)

print(condicao)
