cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
        "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if 0 <= num <= 20:
            print(f"vc digitou o número {cont[num]}")
            break
        print("Tente novamente. ", end="")
    
    opcao = str(input("vc quer continuar?[S/N] ")).strip().upper()
    if opcao == 'N':
        print("programa encerrado")
        break