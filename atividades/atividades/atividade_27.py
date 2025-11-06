# atvd 27
26

texto = str(input("diga a frase: ")).strip()
print("Quantas vezes aparece a letra 'A':",texto.count("A"))
print("Posição da primeira ocorrência de 'A':",texto.find("A")+1)
print("Posição da última ocorrência de 'A':",texto.rfind("A")+1)