'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
Obs.: Com 16, 17 e acima de 65 anos, o voto é OPCIONAL.
'''

def voto(ano_nascimento: int) -> str:
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    texto = f'Com {idade} anos: VOTO '

    if idade < 16:
        return texto + 'NEGADO'
    elif 18 <= idade < 65:
        return texto + 'OBRIGATÓRIO'
    else:
        return texto + 'OPCIONAL'


print('-' * 30)

nascimento = int(input('Em que ano você nasceu: '))
print(voto(nascimento))
