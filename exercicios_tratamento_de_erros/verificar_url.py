import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except (urllib.error.URLError):
    print('Deu Erro!')
else:
    print('tudo ok')
