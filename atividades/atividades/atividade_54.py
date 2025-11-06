# atvd 54
53

frase = str(input("digite a frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)- 1, -1, -1 ):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print("e um palidromo")
else:
    print("a frase n e um palidromo")