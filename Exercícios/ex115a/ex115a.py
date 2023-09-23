'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome
e idade em um arquivo de texto simples. O sistema só vai ter 2 opções:
cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
'''

from arquivo import arquivo_existe, cadastrar, criar_arquivo, ler_arquivo
from menu import cabecalho, menu, leiaInt
from time import sleep

arquivo = 'cursoemvideo.txt'

lista = [
    'Ver pessoas cadastradas',
    'Cadastrar nova pessoa',
    'Sair do sistema'
]

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    resposta = menu(caracter='-', tamanho=46, texto='MENU PRINCIPAL', lista=lista)
    if resposta == 1:
        ler_arquivo(arquivo)
    elif resposta == 2:
        cabecalho(tamanho=46, texto='NOVO CADASTRO')
        nome = input('Digite o nome: ').strip()
        idade = leiaInt('Digite a idade : ')
        cadastrar(nome_arquivo=arquivo, nome=nome, idade=idade)
    elif resposta == 3:
        cabecalho(tamanho=46, texto='SAINDO DO SISTEMA. ATÉ LOGO!')
        break
    else:
        print('Digite uma opção válida.')

    sleep(2)
