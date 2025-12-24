import os
from lib import cabeçalho

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def CriarArquivo(nome):
    
    caminho_pasta = 'ex115'
    caminho_arquivo = os.path.join(caminho_pasta, nome)
    if os.path.exists(caminho_arquivo):
        print(f'O arquivo {caminho_arquivo} já existe!')
    else:
        try:
            with open(caminho_arquivo, 'wt+') as a:
             pass  
        except Exception as e:
            print(f'Houve um ERRO na criação do arquivo! Erro: {e}')
        else:
            print(f'Arquivo {caminho_arquivo} criado com sucesso!')

def LerArquivo(nome):
    caminho_arquivo = os.path.join('ex115', nome)  

    try:
        with open(caminho_arquivo, 'rt') as a:
            cabeçalho('PESSOAS CADASTRADAS')
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

def Cadastrar(arq, nome='Desconhecido', idade=0):
    caminho_arquivo = os.path.join('ex115', arq)
    try:
        a = open(caminho_arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
