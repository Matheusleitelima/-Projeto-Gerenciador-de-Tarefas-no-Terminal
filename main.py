
import funcoes
import dados

tarefas_pendentes = []
tarefas_concluidas = []



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
        funcoes.adicionar_tarefa(nova_tarefa) #a tarefa digitada pelo usuário é adicionada na lista de tarefas.

    elif opcmenu == 2:
        print('Deseja ver as tarefas pendentes (1) ou as concluidas (2)')
        opc_listar = int(input('Digite:'))

        if opc_listar == 1:
            retorno_tela_pendentes = funcoes.mostrar_tarefa_pendentes() #mostrar a função no print.
            print(f'\nTAREFAS PENDENTES: {retorno_tela_pendentes}\n')

        else:
            retorno_tela_concluidas = funcoes.mostrar_tarefa_concluidas() #mostrar a função no print.
            print(f'\nTAREFAS CONCLUIDAS: {retorno_tela_concluidas}\n')


    elif opcmenu == 3:
        tarefa_marcar = input('Qual tarefa deseja marcar como concluida?').lower()
        funcoes.marcar_tarefa_concluidas(tarefa_marcar)

    elif opcmenu == 4:
         funcoes.remover_item_lista()
         

    elif opcmenu == 5:
         print(f'Obrigado por utilizar nosso sistema, volte sempre!')
         break
    
    else:
        print('Ops, opção error. ')
        
        


    
             


