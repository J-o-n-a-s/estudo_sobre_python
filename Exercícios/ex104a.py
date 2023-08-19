'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex.:
numero = leiaInt('Digite um número: ')
'''

def leiaInt(texto: str) -> int:
    while True:
        valor_digitado = input(texto).strip()
        if valor_digitado.isnumeric():
            return int(valor_digitado)
        else:
            print('Erro! Digite um número inteiro válido.')
    
numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}.')
