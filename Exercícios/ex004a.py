dado = input('Digite algo: ')
print(f'O tipo primitivo é: {type(dado)}') # O "input" sempre retorna tipo "str"
print(f'O valor digitado é númérico? {dado.isnumeric()}')
print(f'O valor digitado é somente texto? {dado.isalpha()}')
print(f'O valor digitado é alfanumérico? {dado.isalnum()}')
print(f'O valor digitado é um texto minúsculo? {dado.islower()}')
print(f'O valor digitado é um texto maiúsculo? {dado.isupper()}')
print(f'O valor digitado é um espaço? {dado.isspace()}')
print(f'O valor digitado está capitalizado? {dado.istitle()}')