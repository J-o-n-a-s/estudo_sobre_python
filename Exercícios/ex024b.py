nome = input('Digite o nome de uma cidade: ').strip()
resultado = nome[:5].upper() == 'SANTO'
print(f'O nome da cidade começa com "SANTO"?\n{resultado}.')