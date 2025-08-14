
import dados


def adicionar_tarefa(tarefa): #definindo uma função chamada adicionar_tarefa e tarefa — que será a informação que será adicionada
    dados.tarefas_pendentes.append(tarefa) # adicionar o valor da variável `tarefa ao final da lista.
    with open("tarefas_pendentes.txt", "a", encoding="utf-8") as arquivo:
         arquivo.write(tarefa + "\n")
    print(f'A tarefa "{tarefa}"foi adicionada!\n') #Esse comando mostra uma mensagem na tela, confirmando que a tarefa foi adicionada.
    # Adiciona a tarefa recebida à lista global de tarefas e imprime uma confirmação para o usuário

def mostrar_tarefa_pendentes():
        return dados.tarefas_pendentes

def adicionar_tarefa_concluidas(tarefa_concluida): #definindo uma função chamada adicionar_tarefa e tarefa — que será a informação que será adicionada
    dados.tarefas_concluidas.append(tarefa_concluida) # adicionar o valor da variável `tarefa ao final da lista.
    print(f'A tarefa "{tarefa_concluida}"foi adicionada!\n') #Esse comando mostra uma mensagem na tela, confirmando que a tarefa foi adicionada.
    # Adiciona a tarefa recebida à lista global de tarefas e imprime uma confirmação para o usuário

def mostrar_tarefa_concluidas():
        return dados.tarefas_concluidas

def marcar_tarefa_concluidas(opc_user):
     if opc_user in dados.tarefas_pendentes:
          dados.tarefas_pendentes.remove(opc_user)
          #1° devemos ler as tarefas
          with open("tarefas_pendentes.txt", "r", encoding="utf-8") as arquivo:
               linhas = arquivo.readlines()

            #2° remover os espaços e comparar
               linhas= [linha.strip() for linha in linhas if linha.strip() != opc_user]

            #3° salvar a lista pendentes sem a tarefa concluida
          with open("tarefas_pendentes.txt", "w", encoding= "utf-8") as arquivos:
               for tarefa  in linhas:
                    arquivos.write(tarefa + "\n")
                    
          
          dados.tarefas_concluidas.append(opc_user)
          with open("tarefas_concluidas.txt", "a", encoding="utf-8") as arquivos:
               arquivos.write(opc_user + "\n")
     print(f'a tarefa {opc_user} foi adicionada a lista de concluidas!\n')


def remover_item_lista():
     print('deseja remover da lista de pendentes (1) ou de concluidas (2)?\n')  
     opc_remover = int(input('digite: '))  

     if opc_remover == 1:
          item_remover = input('qual tarefa deseja remover de pendentes?').lower()
          if item_remover in  dados.tarefas_pendentes:
            dados.tarefas_pendentes.remove(item_remover)
             #1° devemos ler as tarefas
            with open("tarefas_pendentes.txt", "r", encoding="utf-8") as arquivo:
               linhas = arquivo.readlines()

            #2° remover os espaços e comparar
               linhas= [linha.strip() for linha in linhas if linha.strip() != item_remover]

            #3° salvar a lista pendentes sem a tarefa concluida
            with open("tarefas_pendentes.txt", "w", encoding= "utf-8") as arquivos:
               for tarefa  in linhas:
                    arquivos.write(tarefa + "\n")    
               print(f'a tarefa {item_remover} foi removido da lista de pendentes!\n')

          else:
               print(f'a tarefa {item_remover} não foi encontrada!')

     else:
          item_remover = input('qual tarefa deseja remover de concluidas?').lower()
          if item_remover in  dados.tarefas_concluidas:
            dados.tarefas_concluidas.remove(item_remover)
             #1° devemos ler as tarefas
            with open("tarefas_concluidas.txt", "r", encoding="utf-8") as arquivo:
               linhas = arquivo.readlines()

            #2° remover os espaços e comparar
               linhas= [linha.strip() for linha in linhas if linha.strip() != item_remover]

            #3° salvar a lista pendentes sem a tarefa concluida
            with open("tarefas_concluidas.txt", "w", encoding= "utf-8") as arquivos:
               for tarefa  in linhas:
                    arquivos.write(tarefa + "\n")
                    
               print(f'a tarefa {item_remover} foi removido da lista de concluidas!\n')

               
          else:
           print(f'a tarefa {item_remover} não foi encontrada!')
