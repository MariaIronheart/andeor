i = int(input("Qual sua idade?: "))
c = input("Você é estudante ou professor? (sim/não): ")
s = input("Qual dia da semana você tem interesse?: ")
valor_ingresso = (20)
if i <= 8:
    print("Você tem 50% de desconto:", valor_ingresso-valor_ingresso*0.5)
if c == "sim":
    print("Você tem desconto de 20%:", valor_ingresso-valor_ingresso*0.2)
if s == "segunda feira" and c == "não":
    print("Você tem 10% de desconto:", valor_ingresso-valor_ingresso*0.1)
if s == "terça-feira" and c == "não":
    print("Você tem 5% de descoto: ", valor_ingresso-valor_ingresso*0.05)
