# atvd 67
66

n = s = nd = 0

while n >= 0:
    n = int(input("digite um numero: "))
    if n == 999:
        break
    s += n
    nd +=1
print(f"vc digitou {nd} numeros e a soma entre ele e {s}")