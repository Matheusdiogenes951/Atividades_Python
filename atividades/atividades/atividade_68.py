# atvd 68
67

tab = 1
n = int(input("digite um numero "))

while tab <= 10:
    print(f"{n} x {tab} = {n * tab}")
    tab += 1
    if n <=0:
        print("o programa encerrou, volter sempre")
        break