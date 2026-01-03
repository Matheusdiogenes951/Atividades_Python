from   datetime import date

dados = dict()
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['Idade'] = date.today().year - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 se nao tem): '))
if dados['CTPS'] != 0:
    dados['Ano de contratacao'] = int(input('Ano de contratacao: '))
    dados['Salario'] = float(input('Salario R$: '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de contratacao'] + 35) - date.today().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
    