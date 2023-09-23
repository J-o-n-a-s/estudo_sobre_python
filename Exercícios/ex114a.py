import urllib.request

try:
    site = urllib.request.urlopen('http://www.progbin.com.br')
except ConnectionResetError:
    print('O site da Progbin Automação não está acessível.')
except Exception as erro:
    print(erro.__class__)
else:
    print('O site da Progbin Automação está acessível.')
    # print(site.read())
