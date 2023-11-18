import random

# функция, выполняющая слияние 2 списков посредством сравнения указателей на элементы списков
def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c

# рекурсивная функция которая делит списки пополам до тех пор пока не получим список из одного элемента,
# в итоге возвращаем список из 2 элементов, отсортированных слиянием
def merge_sort(s):
    if len(s) == 1:
        return s
    else:
        middle = len(s) // 2
        left = merge_sort(s[:middle])
        right = merge_sort(s[middle:])
    return merge_two_list(left, right)


test_list = [random.randint(-100, 100) for i in range(15)]
print(test_list)
print(merge_sort(test_list))

# Сложность: O(n * log(n)) в любом случае