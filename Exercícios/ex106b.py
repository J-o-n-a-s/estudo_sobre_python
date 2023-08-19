'''
Crie um mini-sistema que utilize o Interactive Help do Pythohn.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM", o mini-sistema se encerrará.
Obs.: Utilize cores em seu mini-sistema.
'''

from time import sleep

cores = (
    '\033[m',		# 0 - Sem cores
    '\033[0;30;41',	# 1 - Vermelho
    '\033[0;30;42',	# 2 - Verde
    '\033[0;30;43',	# 3 - Amarelo
    '\033[0;30;44',	# 4 - Azul
    '\033[0;30;45',	# 5 - Roxo
    '\033[7;30'		# 6 - Branco
)

def escreva(caracter: str, texto: str, cor=0) -> None:
    texto = '  ' + texto + '  '
    print(cores[cor], end='')
    print(caracter * len(texto))
    print(texto)
    print(caracter * len(texto))
    print(cores[0], end='')
    sleep(1)


def ajuda(mensagem: str) -> None:
    escreva(caracter='~', texto=f'Acessando o manual do comando "{mensagem}".', cor=4)
    sleep(2)
    print(cores[6], end='')
    help(mensagem)
    print(cores[0], end='')
    

while True:
    escreva(caracter='~', texto='SISTEMA DE AJUDA PyHELP', cor=2)
    funcao = input('Digite uma função ou biblioteca: ').strip()
    
    if funcao.upper() == 'FIM':
        break
    
    ajuda(funcao)

escreva(caracter='~', texto='ATÉ LOGO!', cor=1)
