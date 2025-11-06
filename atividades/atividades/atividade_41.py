# atvd 41
40

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2

if m < 5:
    print("Reprovado! Sua média foi {}".format(m))
elif 5 <= m < 6.9:
    print("Recuperação! Sua média foi de {}".format(m))
else:
    print("Aprovado! Sua média foi de {}".format(m))