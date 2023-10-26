def check(arr):
    brackets = []
    if len(arr) > 2 and arr[-2] in '+-*/':
        raise ValueError("Некорректный ввод!")

    for i in arr:
        if '+)' in ''.join(arr) or '-)' in ''.join(arr) or '*)' in ''.join(arr) or '/)' in ''.join(arr):
            raise ValueError("Некорректный ввод!")
        if i in '([{': 
            brackets.append(i)
        elif i in ')]}':            
            if not brackets:            
                raise ValueError("Некорректный ввод!")
            if (i == ')' and brackets[-1] == '(') or (i == ']' and brackets[-1] == '[') or (i == '}' and brackets[-1] == '{'):
                brackets.pop()
    if brackets:
        raise ValueError("Некорректный ввод!")
    

def evaluate(arr):
    numbers = []
    symbols = []
    streak = 0
    for i in arr:
        if i in '1234567890':
            numbers.append(int(i))
            streak = 0

        elif i in '+-':
            streak += 1
            if len(symbols) == 0:
                symbols.append(i)
            else:
                while len(symbols) != 0 and symbols[-1] in '+-*/':
                    numbers.append(symbols[-1])
                    symbols.pop()
                symbols.append(i)

        elif i in '*/':
            streak += 1
            if len(symbols) == 0 or symbols[-1] in '+-': 
                symbols.append(i)
            else:
                while len(symbols) != 0 and symbols[-1] in '*/':
                    numbers.append(symbols[-1])
                    symbols.pop()
                symbols.append(i)

        elif i == '(':
            symbols.append(i)
        elif i == ')':
            while symbols[-1] != '(':
                numbers.append(symbols[-1])
                symbols.pop()
            symbols.pop()

        elif i == '=':
            while len(symbols) != 0:
                numbers.append(symbols[-1])
                symbols.pop()
        if streak > 1:
            raise ValueError("Некорректный ввод!")
    return numbers

def calculate(arr):
    stack = [] 
    for i in arr:
        if i == '+':
            b = stack.pop()
            a = stack.pop()
            result = a + b
            stack.append(result)
        elif i == "-":
            b = stack.pop()
            a = stack.pop()
            result = a - b
            stack.append(result)
        elif i == "*":
            b = stack.pop()
            a = stack.pop()
            result = a * b
            stack.append(result)
        elif i == "/":
            b = stack.pop()
            a = stack.pop()
            if int(b) == 0:
                raise ZeroDivisionError("Деление на ноль!")
            else:
                result = a / b
                stack.append(result)
        else:
            stack.append(int(i))

    return stack

lst = list(input("Введите пример: "))
if lst[-1] != "=":
    print("Некорректный ввод!")
    exit()
try:
    check(lst)
    print(*calculate(evaluate(lst)))
except (ValueError) as e:
    print(e)
except (ZeroDivisionError) as e:
    print(e)