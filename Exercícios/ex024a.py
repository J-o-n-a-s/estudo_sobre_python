nome = input('Digite o nome de uma cidade: ').strip()
resultado = nome.upper().startswith('SANTO')
print(f'O nome da cidade começa com "SANTO"?\n{resultado}.')