def simple_multipiers(x):
    result = []
    for m in range(100):
        for l in range(100):
            for k in range(100):
                tmp = 3 ** k * 5 ** l * 7 ** m
                if tmp <= x:
                    result.append(tmp)
                else:
                    break
    return result

x = int(input("Введите число х: "))
print("Все числа, удовлетворяющие условию:", end=' ')
print(*sorted(simple_multipiers(x)), sep=", ")