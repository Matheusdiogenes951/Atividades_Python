# atvd 23
22

nome = str(input("qual o seu nome? ")).strip()
primeiro_nome = nome.split()[0]
print("td em maiúsculoe {}".format(nome.upper()))
print("td em minusculo e {}".format(nome.lower()))
print("seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))