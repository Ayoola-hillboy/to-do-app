#to do variables
user_prompt = "enter todo:"

list_todo = []
#Tell user to enter a todo list

from function import get_todos, write_todos
import time
time_now= time.strftime("%b %d, %Y %H: %M: %S")
print("KALOLOALAO")
print ("Time and date information is", time_now)
while True:
    answer=input ("type add,show, end ,edit, complete followed by the content you want to apply action to: ")
    answer= answer.strip()



    if answer.startswith("add") :
        add_todo =  answer [4:] + "\n"

#use open function to open file and read it so it can keep it and then closed it

        list_todo = get_todos()


#appends new activity to my list
        list_todo.append(add_todo)
#this will open the file and write my new items into the file without deleting the previous ones

        write_todos(list_todo)

    elif "show" in answer:
        list_todo = get_todos()

        for index, things in enumerate (list_todo):
            things = things.strip()
            things = things.title()
            remove_space= f"{index+1}.{things}"
            print(remove_space)

    elif answer.startswith("edit"):
        try:
            number_to_editx = int (answer[5:])
            number_to_edit =number_to_editx - 1

            list_todo = get_todos()

            replacement = input ("what is your new todo?")
            list_todo[number_to_edit] = replacement + "\n"

            write_todos(list_todo)
        except ValueError:
            print("command is not valid")
            continue

    elif answer.startswith("complete"):
        try:
            to_complete= int (answer [9:])
            remove_index = to_complete - 1
            to_remove = list_todo[remove_index].strip('\n')

            list_todo = get_todos()

            list_todo.pop(remove_index)

            write_todos(list_todo)

            message_to_user = f"Todo {to_remove} was removed from the list"
            print (message_to_user)
        except IndexError:
            print ("No item with that index")
            continue

    elif "end" in answer:
        break

    else:
        print ("fuck you")


print ("Bye")







