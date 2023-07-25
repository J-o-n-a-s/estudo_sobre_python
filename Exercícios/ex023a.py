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