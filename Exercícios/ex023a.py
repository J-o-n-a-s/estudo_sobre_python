'''
Crie um programa que leia um número entre 0 e 9999 e mostre na tela cada um dos dígitos separadamente.
 - Exemplo "1234":
   - Milhar = 1
   - Centena = 2
   - Dezena = 3
   - Unidade = 4
'''

numero = int(input('Digite um número entre 0 e 9999: '))
milhar = numero // 1000
centena = (numero - (milhar * 1000)) // 100
dezena = (numero - (milhar * 1000 + centena * 100)) // 10
unidade = (numero - (milhar * 1000 + centena * 100 + dezena * 10)) // 1
print(
    f'''
    Milhar = {milhar}
    Centena = {centena}
    Dezena = {dezena}
    Unidade = {unidade}
    '''
)
