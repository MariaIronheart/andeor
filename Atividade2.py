idade = int(input("Digite sua idade: "))
a = (input("Você tem autorização? (sim/não): "))

if (idade >= 18 and a == "não") or a == "sim":
    print("Você pode entrar na festa")
else: 
    print("Você não pode entrar na festa")