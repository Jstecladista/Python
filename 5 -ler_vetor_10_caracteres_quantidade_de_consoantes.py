caracteres = []
i = 0
consoantes = 0
while i <= 10:
    letras = str(input("Digite um caractere: ")).lower()
    caracteres.append(letras)
    if letras != "a" and letras != "e" and letras and "i" and letras != "o" and letras != "u":
        consoantes += 1
    i += 1
print("A Quantidade de consoantes é: ", consoantes)