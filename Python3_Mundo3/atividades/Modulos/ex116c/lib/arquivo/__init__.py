from Python3_Mundo3.atividades.Modulos.ex116b.lib.interface import cabecalho


def arquivoExiste(note):
    try:
        a = open(note, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ouve um erro')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Ouve um erro')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Nome: {dado[0]:<30} Idade: {dado[1]:>3}')

    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Ouve um erro')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Ouve um erro')
        else:
            print(f'novo registro de {nome} criado com sucesso')
            a.close()
