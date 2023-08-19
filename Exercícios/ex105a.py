'''
Crie um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional).
Adicione também as docstrings da função.
'''

def notas(* valores_notas: int, situacao: bool =False) -> dict:
    '''
    -> Função para analisar notas e situações do aluno.
    :param valores_notas: Uma ou mais notas do aluno (aceita várias notas).
    :param situacao: (Opcional) Adiciona ou não a situação do aluno.
    :return: Retorna o dicionário com as informações do aluno.
    '''
    retorno = {}
    retorno['total'] = len(valores_notas)
    retorno['maior'] = max(valores_notas)
    retorno['menor'] = min(valores_notas)
    retorno['media'] = sum(valores_notas) / len(valores_notas)
    
    if situacao:
        if retorno['media'] < 5.0:
            retorno['situacao'] = 'RUIM'
        elif retorno['media'] >= 7.0:
            retorno['situacao'] = 'BOA'
        else:
            retorno['situacao'] = 'REGULAR'
    
    return retorno

print(notas(5.5, 4.5, 6.6, 8.2, 7.0, situacao=True), end='\n\n')
help(notas)
