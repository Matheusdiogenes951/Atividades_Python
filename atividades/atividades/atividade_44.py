# atvd 44
43

peso = float(input("digite seu peso: "))
altura = float(input("diga sua atura"))
imc = peso / (altura**2)
print("o imc dessa pessoa e {:2f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <imc <= 25:
    print("peso ideal")
elif 25 < imc <= 30:
    print("sobrepeso")
elif 30 < imc <= 40:
    print("obesidade")
elif imc >40:
    print("obesidade")