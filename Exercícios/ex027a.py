nome = input('Digite seu nome completo: ').strip()
nome_completo = nome.split()
print(f'Seu primeiro nome é {nome_completo[0]} e seu último nome é {nome_completo[len(nome_completo) - 1]}.')