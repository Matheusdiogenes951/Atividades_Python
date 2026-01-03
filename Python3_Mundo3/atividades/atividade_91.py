aluno = {}

nome = str(input("Nome: "))
Media = float(input('Media: '))

if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situacao'] = 'Recuperacao'
else:
    aluno['Situacao'] = 'Reprovado'

print('-=' * 30)

for k, v in aluno.items():
    print(f' - {k} e igual a {v}')
