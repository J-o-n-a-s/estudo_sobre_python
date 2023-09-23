'''
Reescreva a função leiaInt() que fizemos no exercício 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''


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


def leiaFloat(texto: str) -> float:
    while True:
        try:
            valor_digitado = float(input(texto))
        except (ValueError, TypeError):
            print('Erro! Digite um número float válido.')
        except KeyboardInterrupt:
            print('\nUsuário preferiu não digitar esse número.')
            return 0.0
        else:
            return valor_digitado


numero_inteiro = leiaInt('Digite um número inteiro: ')
numero_float = leiaFloat('Digite um número float: ')
print(f'O valor inteiro digitado foi {numero_inteiro} e o real foi {numero_float}.')
