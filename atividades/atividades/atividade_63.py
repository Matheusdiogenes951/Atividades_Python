# atvd 63
62

primeiro_termo = int(input("Digite o primeiro termo da PA: "))

razao = int(input("Digite a razão da PA: "))

termo_atual = primeiro_termo
contador = 1
total = 0
mais = 10
print("\nOs 10 primeiros termos da PA são:")
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"{contador}° Termo = {termo_atual}")
        termo_atual += razao
        contador += 1
    mais = int(input("quantos termos vc quer mostrar a mais? "))