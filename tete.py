import urllib.request

x = urllib.request.urlopen('https://www.google.com.br')
print(x.read)