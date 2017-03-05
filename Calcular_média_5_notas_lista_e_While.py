notas = [4,10,3,8,3]

contador = 0
soma = 0

while contador <= 4:
    soma = soma + notas[contador]
    contador = contador + 1

print("A Média das 5 notas do aluno é ", soma/contador)