#LISTAS. PROJETO CRIADO NA mimo.org
"""LISTA VAZIA NO QUAL O USUÁRIO TEM 3 OPÇÕES:
1) ADICIONAR TAREFA;
2) REMOVER ULTIMA TAREFA;
3) SAIR DO LOOP"""
todo_list = []
while True:
  
  if not todo_list:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
  print("Options:")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit")
  choice = input("Enter with your choice 1), 2) or 3): ")

  if choice == "1":
    new_task = input("Insert a new task: ")
    todo_list.append(new_task)
    print("Adding task")
  elif choice == "2":
    print(todo_list)
    if len(todo_list) == 0:
      print("empty")
    else:
      todo_list.pop()
      print("Removing task")
  elif choice == "3":
    print("Quitting")
    break