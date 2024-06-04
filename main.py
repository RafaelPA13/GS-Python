#Cadastro de lixo
def adicao(opcao):
    if opcao == 'plástico':
        adicionar_lixo('plástico', plastico)
    elif opcao == 'vidro':
        adicionar_lixo('vidro', vidro)
    elif opcao == 'metal':
        adicionar_lixo('metal', metal)
    else:
        adicionar_lixo('madeira', madeira)      

#Remoção de lixo
def remocao(opcao):
    if opcao == 'plástico':
        remover_lixo('plástico', plastico)
    elif opcao == 'vidro':
        remover_lixo('vidro', vidro)
    elif opcao == 'metal':
        remover_lixo('metal', metal)
    else:
        remover_lixo('madeira', madeira)  

#Adiciona um lixo de uma lista
def adicionar_lixo(tipo, lista):
    #Armazenando o que foi digitado no input
    lixo = input(f'Digite o lixo de {tipo} para ser adicionado: ')

    #Verifica se o que foi digitado não é um número
    while lixo.isnumeric():
        print('Você não pode digitar um número')
        lixo = input(f'Digite o lixo de {tipo} para ser adicionado: ')

    #Aciciona o lixo na sua respectiva lista
    lista.append(lixo)
    print(lista)

#Remove um lixo de uma lista
def remover_lixo(tipo, lista):
    #Armazenando o que foi digitado no input
    lixo = input(f'Digite o lixo de {tipo} para ser removido: ')

    #Verifica se o que foi digitado não é um número
    while lixo.isnumeric():
        print('Você não pode digitar um número')
        lixo = input(f'Digite o lixo de {tipo} para ser removido: ')

    #Remove o lixo na sua respectiva lista
    lista.remove(lixo)
    print(lista)

#Verificação do conteúdo da lista
def tipos_lixo(lista, buscar):
    for elem in lista:
        if elem == buscar:
            return True
    return False

#Lista de opções  
opcoes = ['plástico', 'vidro', 'metal', 'madeira']

#Listas para cada tipo de lixo
plastico = []
vidro = []
metal = []
madeira = []
    
while True:
    print('Bem Vindo!')
    #Definindo mensagem de erro
    msg_erro = ' '.join(opcoes)
    msg_erro = f'Insira uma das opções\n{msg_erro}'

    #Armazenando o que foi digitado no input
    opcao = input('Digite o tipo do lixo encontrado\n-> ')
            
    #Força a digitar somente os tipos de lixo presentes na lista
    while not tipos_lixo(opcoes, opcao):
        print(msg_erro)
        opcao = input('Digite o tipo do lixo encontrado\n-> ')
            
    #Verifica qual será a modificada
    acao = input('O que deseja fazer hoje\nAdicionar dados\nRemover dados\n-> ')
    if acao == 'Adicionar' or acao == 'adicionar':
        adicao(opcao)
    else:
        remocao(opcao)
            
    #Verifica se quer continuar
    continuar = input('Deseja continuar: ')  
        
    if continuar == 'Não' or continuar == 'não':
        print('Obrigado pela visita')
        break
        