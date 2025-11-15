# atvd 37
36

import math
casa = float(input("qual o valor da casa? "))
salario = int(input("Qual o seu salario? "))
anos = int(input("quantos anos vc vai pagar? "))
prestacao = casa / (anos * 12)

print("ara pagar uma casa de {} em {} a prestacao sera de {} ".format(casa, anos, prestacao))



if prestacao > salario * 0.30:
    print("vc nao pode comprar essa casa")
else:
    print("vc pode comprar essa casa")