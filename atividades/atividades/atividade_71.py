# atvd 71
70

total = 0
mc = 0
mb = ''
pb = 0

while True:
    nome = str(input("Nome do produto: ")).strip().capitalize()
    preco = float(input("Preço do produto: R$ "))

    total += preco

    if preco > 1000:
        mc += 1

    if pb == 0 or preco < pb:
        pb = preco
        mb = nome

    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()
    if opcao == 'N':
        print("\nPrograma encerrado.")
        break

print(f"Total gasto na compra: R$ {total:.2f}")
print(f"Produtos que custam mais de R$1000: {mc}")
print(f"Produto mais barato: {mb} (R$ {pb:.2f})")