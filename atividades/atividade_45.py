# atvd 45
44

preco_normal = float(input("Digite o preço normal do produto: R$ "))

print("\nEscolha a condição de pagamento:")
print("1. À vista em dinheiro/cheque (10% de desconto)")
print("2. À vista no cartão (5% de desconto)")
print("3. Em até 2x no cartão (preço normal)")
print("4. 3x ou mais no cartão (20% de juros)")

opcao = input("Digite o número da opção desejada: ")

if opcao == '1':
    desconto = preco_normal * 0.10
    valor_final = preco_normal - desconto
    print(f"\nValor a pagar: R$ {valor_final:.2f}")
elif opcao == '2':
    desconto = preco_normal * 0.05
    valor_final = preco_normal - desconto
    print(f"\nValor a pagar: R$ {valor_final:.2f}")
elif opcao == '3':
    valor_final = preco_normal
    print(f"\nValor a pagar: R$ {valor_final:.2f}")
elif opcao == '4':
    juros = preco_normal * 0.20
    valor_final = preco_normal + juros
    print(f"\nValor a pagar: R$ {valor_final:.2f}")
else:
    print("\nOpção inválida.")