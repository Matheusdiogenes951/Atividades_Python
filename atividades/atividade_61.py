# atvd 61
60

numero = int(input("Digite um número inteiro: "))
fatorial = 1
contador = numero

if numero < 0:
   print("Fatorial não é definido para números negativos")

elif numero == 0 or numero == 1:
   print(f"O fatorial de {numero} é 1")
else:
   while contador > 0:
       fatorial = fatorial * contador
       contador = contador - 1
   print(f"O fatorial de {numero} é {fatorial}")