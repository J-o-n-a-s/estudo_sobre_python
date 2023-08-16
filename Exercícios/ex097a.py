'''
Crie um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, mundo!')
Saída:
~~~~~~~~~~~~~~~
  Olá, mundo!
~~~~~~~~~~~~~~~
'''

def escreva(caracter: str, texto: str):
    texto = '  ' + texto + '  '
    print(caracter * len(texto))
    print(texto)
    print(caracter * len(texto))

escreva('~', 'Olá, mundo!')
escreva('-', 'Gustavo Guanabara')
escreva('#', 'CeV')
escreva('*', 'Jonas!')
