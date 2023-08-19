'''
Crie um mini-sistema que utilize o Interactive Help do Pythohn.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM", o mini-sistema se encerrará.
Obs.: Utilize cores em seu mini-sistema.
'''

from time import sleep

def escreva(caracter: str, texto: str) -> None:
    texto = '  ' + texto + '  '
    print(caracter * len(texto))
    print(texto)
    print(caracter * len(texto))
    sleep(1)


def ajuda(mensagem: str) -> None:
    escreva(caracter='~', texto=f'Acessando o manual do comando "{mensagem}".')
    sleep(2)
    help(mensagem)
    

while True:
    escreva(caracter='~', texto='SISTEMA DE AJUDA PyHELP')
    funcao = input('Digite uma função ou biblioteca: ').strip()
    
    if funcao.upper() == 'FIM':
        break
    
    ajuda(funcao)

escreva(caracter='~', texto='ATÉ LOGO!')
