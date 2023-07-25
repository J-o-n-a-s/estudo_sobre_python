numero = int(input('Digite um número entre 0 e 9999: '))
milhar = numero // 1000
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10
print(
    f'''
    Analizando o número {numero}
    Milhar = {milhar}
    Centena = {centena}
    Dezena = {dezena}
    Unidade = {unidade}
    '''
)