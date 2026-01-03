aluno = {'nome': '', 'Media': 0,}

nome = str(input("Nome: "))
Media = float(input('Media: '))

aluno['nome'] = nome
aluno['Media'] = Media

print('-=' * 30)

print(f'Nome e igual a {aluno["nome"]}]')

print(f'Media e igual a {aluno["Media"]}]')

if aluno['Media'] >= 7:
    print('Situacao e aprovado')
else:
    print('Situacao e reprovado')