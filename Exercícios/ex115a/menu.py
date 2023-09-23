TAMANHO_PADRAO = 42


def linha(caracter: str = '-', tamanho: int = TAMANHO_PADRAO) -> str:
    return caracter * tamanho


def cabecalho(caracter: str = '-', tamanho: int = TAMANHO_PADRAO, texto: str = None):
    print(linha(caracter=caracter, tamanho=tamanho))
    print(f'{texto.center(len(linha(caracter=caracter, tamanho=tamanho))).upper()}')
    print(linha(caracter=caracter, tamanho=tamanho))


def leiaInt(texto: str) -> int:
    while True:
        try:
            valor_digitado = int(input(texto))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nUsuário preferiu não digitar esse número.')
            return 0
        else:
            return valor_digitado


def menu(caracter: str = '-', tamanho: int = TAMANHO_PADRAO, texto: str = '', lista: list = []) -> int:
    cabecalho(caracter, tamanho, texto)
    contador = 1
    for item in lista:
        print(f'{contador} - {item}')
        contador += 1

    print(linha(caracter=caracter, tamanho=tamanho))
    return leiaInt('Digite sua opção: ')
