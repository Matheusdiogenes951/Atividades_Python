# atvd 35
34

salario_atual = float(input("Digite o salário atual: "))
if salario_atual > 1250:
    aumento = salario_atual * 0.10
else:
    aumento = salario_atual * 0.15

novo_salario = salario_atual + aumento
print(f"Salário atual: R$ {salario_atual:.2f}")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")