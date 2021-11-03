import json
import os

def escreverArquivoJSON(local_arquivo, lista):
    file = open(local_arquivo, 'w', encoding='utf8')
    json.dump(lista, file)
    file.close()

def lerArquivoJSON(local_arquivo):
    with open(local_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def salvarProdutoEmLista(variavel1, variavel2, variavel3, variavel4, lista):
    produto = {
        'codigo': variavel1,
        'nome': variavel2,
        'descricao': variavel3,
        'valor': variavel4
    }
    lista.append(produto)

def criarPrintClsPause(string):
    os.system('cls')
    print('-'*32 + f'\n{string}\n' + '-'*32)
    os.system('pause')
    os.system('cls')

def printMessage(string, numeroDeIfensCima, numeroDeIfensBaixo):
    print('-'*numeroDeIfensCima + f'\n{string}\n' + '-'*numeroDeIfensBaixo)

def criarListaVaziaEmJSON(local_arquivo):
    if os.stat("produtos.json").st_size == 0: # Irá verificar se o arquivo está vazio
        lista_vazia = []
        escreverArquivoJSON(local_arquivo, lista_vazia)