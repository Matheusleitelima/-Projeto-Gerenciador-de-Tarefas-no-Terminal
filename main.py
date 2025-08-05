
lista_tarefa = []


def adicionar_tarefa(tarefa): #definindo uma função chamada adicionar_tarefa e tarefa — que será a informação que será adicionada
    lista_tarefa.append(tarefa) # adicionar o valor da variável `tarefa ao final da lista.
    print(f'A tarefa "{tarefa}"foi adicionada!') #Esse comando mostra uma mensagem na tela, confirmando que a tarefa foi adicionada.
    # Adiciona a tarefa recebida à lista global de tarefas e imprime uma confirmação para o usuário



def mostrar_tarefa():
        return lista_tarefa 

while True:
    print('==MENU==')
    print('1. Adicionar tarefa')
    print('2. Listar tarefas')
    print('3. Marcar tarefa como concluída')
    print('4. Remover tarefa')
    print('5. Sair')
    opcmenu = int(input("Digite a opção desejada:"))

    if opcmenu == 1:
        nova_tarefa = input("Qual tarefa deseja adicionar:")
        adicionar_tarefa(nova_tarefa) #a tarefa digitada pelo usuário é adicionada na lista de tarefas.

    elif opcmenu == 2:
        retorno_tela = mostrar_tarefa() #mostrar a função no print.
        print(retorno_tela)


