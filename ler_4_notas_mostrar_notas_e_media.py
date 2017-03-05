notas = []
i = 0
soma = 0
while i <= 3:
    n = float(input("Digite a nota: "))
    notas.append(n)
    soma = soma + n
    i += 1

print("As notas do aluno foram: ", notas)
print(" ")
print("A Média das 4 notas do aluno é: ", soma/i)
