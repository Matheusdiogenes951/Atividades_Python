# atvd 52
51

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo_atual = primeiro_termo
contador = 1

print("\nOs 10 primeiros termos da PA são:")
while contador <= 10:
    print(f"{contador}° Termo = {termo_atual}")
    termo_atual += razao
    contador += 1