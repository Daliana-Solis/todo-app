import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("\nType add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] +'\n'
        to_do = functions.get_todos()
        to_do.append(todo)
        functions.write_todos(to_do)



    elif user_action.startswith('show'):
        to_do = functions.get_todos()

        for number_item, each_to_do in enumerate(to_do):
            each_to_do = each_to_do.strip("\n")
            print( f"{number_item+1}. {each_to_do}")




    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            new_to_do = input("Enter new to do: ")

            to_do = functions.get_todos()

            to_do[number-1] = new_to_do + '\n'

            functions.write_todos(to_do)
        except ValueError:
            print("Your command is not valid.")
            continue




    elif user_action.startswith('complete'):
        try:
            completed_task_num = int(user_action [9:])
            to_do = functions.get_todos()

            remove_item = to_do[completed_task_num-1].strip('\n')
            to_do.pop(completed_task_num-1)

            functions.write_todos(to_do)
            print(f"To-do {remove_item} was removed from the list")
        except ValueError:
            continue
        except IndexError:
            print("There is no item with that number.")
            continue




    elif user_action.startswith('exit'):
        break

    else: #if none of the commands match previous cases, it will enter this case
        print("Invalid command. Try again.")

print('bye')



