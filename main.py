
tarefas_pendentes = []
tarefas_concluidas = []


def adicionar_tarefa(tarefa): #definindo uma função chamada adicionar_tarefa e tarefa — que será a informação que será adicionada
    tarefas_pendentes.append(tarefa) # adicionar o valor da variável `tarefa ao final da lista.
    print(f'A tarefa "{tarefa}"foi adicionada!\n') #Esse comando mostra uma mensagem na tela, confirmando que a tarefa foi adicionada.
    # Adiciona a tarefa recebida à lista global de tarefas e imprime uma confirmação para o usuário

def mostrar_tarefa_pendentes():
        return tarefas_pendentes

def adicionar_tarefa_concluidas(tarefa_concluida): #definindo uma função chamada adicionar_tarefa e tarefa — que será a informação que será adicionada
    tarefas_concluidas.append(tarefa_concluida) # adicionar o valor da variável `tarefa ao final da lista.
    print(f'A tarefa "{tarefa_concluida}"foi adicionada!\n') #Esse comando mostra uma mensagem na tela, confirmando que a tarefa foi adicionada.
    # Adiciona a tarefa recebida à lista global de tarefas e imprime uma confirmação para o usuário

def mostrar_tarefa_concluidas():
        return tarefas_concluidas

def marcar_tarefa_concluidas(opc_user):
     if opc_user in tarefas_pendentes:
          tarefas_pendentes.remove(opc_user)
          tarefas_concluidas.append(opc_user)
     print(f'a tarefa {opc_user} foi adicionada a lista de concluidas!\n')           

        


while True:
    print('==MENU==')
    print('1. Adicionar tarefa')
    print('2. Listar tarefas')
    print('3. Marcar tarefa como concluída')
    print('4. Remover tarefa')
    print('5. Sair')
    opcmenu = int(input("Digite a opção desejada:"))

    if opcmenu == 1:
        nova_tarefa = input("Qual tarefa deseja adicionar:").lower()
        adicionar_tarefa(nova_tarefa) #a tarefa digitada pelo usuário é adicionada na lista de tarefas.

    elif opcmenu == 2:
        print('Deseja ver as tarefas pendentes (1) ou as concluidas (2)')
        opc_listar = int(input('Digite:'))

        if opc_listar == 1:
            retorno_tela_pendentes = mostrar_tarefa_pendentes() #mostrar a função no print.
            print(f'\nTAREFAS PENDENTES: {retorno_tela_pendentes}\n')

        else:
            retorno_tela_concluidas = mostrar_tarefa_concluidas() #mostrar a função no print.
            print(f'\nTAREFAS CONCLUIDAS: {retorno_tela_concluidas}\n')


    elif opcmenu == 3:
        tarefa_marcar = input('Qual tarefa deseja marcar como concluida?').lower()
        marcar_tarefa_concluidas(tarefa_marcar)


    
        
