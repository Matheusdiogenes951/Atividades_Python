# atvd 58
57

sexo = ''
while not (sexo == 'F'  or sexo == 'M'):
    sexo = str(input("Qual o seu sexo? [M/F] ")).upper()[0].strip()
    if sexo not in ['M', 'F']:
        print("digite novamente: ")
print("Seu Sexo e {}".format(sexo))
print("FIM")