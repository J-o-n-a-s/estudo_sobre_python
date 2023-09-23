from menu import cabecalho


def arquivo_existe(nome_arquivo: str) -> bool:
    try:
        arquivo = open(nome_arquivo, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome_arquivo: str):
    try:
        arquivo = open(nome_arquivo, 'wt+')
        arquivo.close()
    except:
        print('Ocorreu um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo "{nome_arquivo}" criado com sucesso!')


def ler_arquivo(nome_arquivo: str):
    try:
        arquivo = open(nome_arquivo, 'rt')
    except:
        print('Ocorreu um Erro ao ler o arquivo!')
    else:
        cabecalho(tamanho=46, texto='PESSOAS CADASTRADAS')
        for linha in arquivo:
            dados = linha.replace('\n', '').split(';')
            print(f'{dados[0]:<36}{dados[1]:>3} anos')
        arquivo.close()


def cadastrar(nome_arquivo: str, nome: str = 'Desconhecido', idade: int = 0):
    try:
        arquivo = open(nome_arquivo, 'at')
    except:
        print('Ocorreu um Erro ao ler o arquivo!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Ocorreu um ERRO na escrita dos dados!')
        else:
            print(f'{nome} cadastrado com sucesso!')

