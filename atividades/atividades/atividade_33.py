# atvd 33
32

ano = int(input("Qual ano você quer saber se é bissexto? "))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano é bissexto")
else:
    print("O ano é normal")