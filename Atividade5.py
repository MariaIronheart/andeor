a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))
c = int(input("Insira o terceiro número: "))

if (a > b+c or b > a+c) or c > a+b:
    print("Pelo menos um do números é mais que a soma dos outros dois")
else:
    print("Nenhum dos números é maior que a soma")