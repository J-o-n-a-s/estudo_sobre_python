'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expressao = input('Digite uma expressão: ').strip()
resultado = False
conta_abre = 0
conta_fecha = 0

if expressao.count('(') != expressao.count(')'):
    resultado = True
else:
    for caracter in expressao:
        if caracter == '(':
            conta_abre += 1
        
        if caracter == ')':
            conta_fecha += 1
            
        if conta_abre < conta_fecha:
            resultado = True
            break

if resultado:
    print(f'Sua expressão é inválida!')
else:
    print('Sua expressão é válida!')
