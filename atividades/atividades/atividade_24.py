# atvd 24
23

num = int(input("diga um numero de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("seu numero tem {} unidades".format(u))
print("seu numero tem {} dezenas".format(d))
print("seu numero tem {} centenas".format(c))
print("seu numero tem {} milhares".format(m))