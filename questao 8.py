a = int(input("Atribua um valor para A: "))
b = int(input("Atribua um valor para B: "))
c = int(input("Atribua um valor para C: "))

if a != b and b != c and a != c:
    valores = [a, b, c]
    valores.sort(reverse=True)

    print("Valores em ordem decrescente")
    for valor in valores:
        print(valor)
else:
    print("Os valores precisam ser diferentes")