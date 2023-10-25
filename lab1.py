def is_right_brackets(string):
    brackets_storage = [] 
    
    for i in string:
        if i in '([{':
            brackets_storage.append(i)
        elif i in ')]}':
            if len(brackets_storage) == 0:
                return False
            for j in brackets_storage:
                if i == ')' and j == '(' or i == ']' and j == '[' or i == '}' and j == '{': 
                    brackets_storage.pop(-1)
                    break

    if len(brackets_storage) == 0:
        return True
    else:
        return False

string = input("Введите строку: ")

if len(string)==0 or not is_right_brackets(string):
    print("Строка не существует")
else:
    print("Строка существует")