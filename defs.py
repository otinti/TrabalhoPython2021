import json
import os

local_arquivo = 'C:\\'

def escreverArquivoJSON(lista):
    file = open(local_arquivo, 'w', encoding='utf8')
    json.dump(lista, file)
    file.close()

def lerArquivoJSON():
    with open(local_arquivo, 'r', encoding='utf8') as f:
        return json.load(f)

def salvarProdutoEmLista(lista):
    codigo = int(input('Código: '))
    nome = input('Nome: ')
    descricao = input('Descrição: ')
    valor = float(input('Valor: '))
    produto = {
        'codigo': codigo,
        'nome': nome,
        'descricao': descricao,
        'valor': valor
    }
    lista.append(produto)

def criarPrintClsPause(string):
    os.system('cls')
    print('-'*32 + f'\n{string}\n' + '-'*32)
    os.system('pause')
    os.system('cls')

def criarListaVazia():
    if os.stat("produtos.json").st_size == 0: # Irá verificar se o arquivo está vazio
        lista_vazia = []
        escreverArquivoJSON(lista_vazia)