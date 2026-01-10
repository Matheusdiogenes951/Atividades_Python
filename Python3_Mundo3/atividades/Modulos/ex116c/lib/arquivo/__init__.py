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

def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Ouve um erro')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()

def cadastrar(arquivo, nome='desconhecido', idade=0):
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