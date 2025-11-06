# atvd 16
15
kp = float(input("quantos km foram percorridos pelo carro? "))
da = int(input("diga por quantos dias ele foi alugado; "))

pa = (60*da) + (kp*0.15)

print("o carro rodou {} e foi alugado por {} dias, a conta sera de {}".format(kp, da, pa))