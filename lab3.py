from math import log


def simple_multipiers(x):
    result = []
    for m in range(int(log(x, 7)) + 1):
        for l in range(int(log(x, 5)) + 1):
            for k in range(int(log(x, 3)) + 1):
                tmp = 3 ** k * 5 ** l * 7 ** m
                if tmp <= x:
                    result.append(tmp)
                else:
                    break
    return result

x = int(input("Введите число х: "))
print("Все числа, удовлетворяющие условию:", end=' ')
print(*sorted(simple_multipiers(x)), sep=", ")