idade = int(input("Digite sua idade: "))
a = input("Você é alfabetizada/o? (sim/não): ")

if idade > 25 and a == "sim":
    print("Você é alfabetizada e tem mais de 25 anos.")
else:
    print("Você não é maior que 25 ou alfabetizada.")