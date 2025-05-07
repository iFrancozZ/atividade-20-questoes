peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))

imc = peso / (altura ** 2)
print(imc)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.6 <=imc <= 24.9:
    print("Peso ideal")
elif 25.0 <= imc <= 29.9:
    print("Levemente acima do peso")
elif 30.0 <=imc <= 34.9:
    print("Obesidade ra 1") 
elif 35.0 <=imc <= 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")
