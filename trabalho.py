import defs
import os
import sys

lista_produtos = []
codigo = valor = 0
nome = descricao = ''

# Limpar console - Start
def limparConsole(pause):
    if pause == True:
        os.system('pause') # Pressione qualquer tecla para continuar. . .
    os.system('cls')
# Limpar console - End

local_arquivo = '.\\produtos.json' # Local do arquivo JSON será na mesma pasta do trabalho.py

defs.criarListaVaziaEmJSON(local_arquivo) # Caso o arquivo estiver vazio, irá criar uma lista vazia (no arquivo) --- Irá evitar erros de arquivo vazio no código
limparConsole(False)
while True:
    menu_inicial = input('\n' + '≡'*5 + 'Menu' + '≡'*5 + '\n[ 1 ]Cadastrar produtos\n[ 2 ]Consultar produtos por faixa de preço\n[ 3 ]Gravar produtos em arquivo\n[ 4 ]Carregar produtos do arquivo\n[ 5 ]Sair\nOpção: ')
    limparConsole(False)

    if menu_inicial == '5': # Sair do programa
        while menu_inicial != lista_produtos:
            msg_de_confirmacao = input('Voce realmente deseja sair? (S/N) => ')
            if msg_de_confirmacao.upper() == 'S':
                defs.printMessage('Programa fechado.', 32, 32)
                sys.exit() # Fechará todo o programa
            elif msg_de_confirmacao.upper() == 'N':
                limparConsole(False)
                break
            else:
                print('[ Erro ] - Não foi possível prosseguir com o procedimento, por favor, pressione a letra correta.')

    elif menu_inicial == '1': # Cadastrar produto
        limparConsole(False)
        defs.printMessage('Cadastrar produto', 0, 32)

        codigo = input('Código: ')
        nome = input('Nome: ')
        descricao = input('Descrição: ')
        valor = float(input('Valor: '))

        defs.salvarProdutoEmLista(codigo, nome, descricao, valor, lista_produtos)
        defs.criarPrintClsPause('Produto cadastrado com sucesso.\nATENÇÃO: Se deseja salvar os produtos cadastrados, não esqueça de selecionar o opção 3 no menu para arquiva-los.')

    elif menu_inicial == '2': # Consultar produtos por faixa de preço
        defs.printMessage('Insira os valores que procura', 0, 32)

        while menu_inicial != lista_produtos:
            preco_minimo = float(input('Preço mínimo: '))
            preco_maximo = float(input('Preço máximo: '))
            if preco_maximo < preco_minimo:
                limparConsole(False)
                print('[ Erro ] - O preço máximo não pode ser menor do que o preço mínimo.')
            else:
                break
            
        limparConsole(False)
        print(f'Produtos    Preco mínimo: {preco_minimo}    Preço máximo: {preco_maximo}')
        print('-'*60)
        ordenar_lista = sorted(defs.lerArquivoJSON(local_arquivo), key=lambda x: x['valor'], reverse=False)
        for j in ordenar_lista:
            if preco_minimo <= j['valor'] and preco_maximo >= j['valor']:
                print(f'Código: {j["codigo"]}\nNome: {j["nome"]}\nDescrição: {j["descricao"]}\nValor: {j["valor"]}')
                print('-'*60)
        limparConsole(True)

    elif menu_inicial == '3': # Gravar produtos em arquivo
        defs.escreverArquivoJSON(local_arquivo, lista_produtos)
        defs.criarPrintClsPause('Produto(s) salvo(s) com sucesso.')
    
    elif menu_inicial == '4': # Carregar produtos do arquivo
        defs.printMessage('Produtos', 0, 60)
        ordenar_lista = sorted(defs.lerArquivoJSON(local_arquivo), key=lambda x: x['codigo'], reverse=False)
        for c in ordenar_lista:
            print(f'Código: {c["codigo"]}\nNome: {c["nome"]}\nDescrição: {c["descricao"]}\nValor: {c["valor"]}')
            print('-'*60)
        limparConsole(True)

    else: # Se a opção digitada for diferente de 1 a 5, não irá fechar o programa e ira disparar uma mensagem de erro
        print('[ Erro ] - Não foi possível prosseguir com o procedimento, por favor, pressione o número correto.')