from random import randint
def siftDown(lst, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper:
            if lst[i] >= max(lst[l], lst[r]):
                break
            elif lst[l] > lst[r]:
                lst[i], lst[l] = lst[l], lst[i]
                i = l
            else:
                lst[i], lst[r] = lst[r], lst[i]
                i = r
        elif l < upper:
            if lst[l] > lst[i]:
                lst[l], lst[i] = lst[i], lst[l]
                i = l
            else:
                break
        elif r < upper:
            if lst[r] > lst[i]:
                lst[r], lst[i] = lst[i], lst[r]
                i = r
            else:
                break
        else:
            break


def heapsort(lst):
    for j in range((len(lst) - 2) // 2, -1, -1):
        siftDown(lst, j, len(lst))

    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        siftDown(lst, 0, end)


#lst = list(map(int, input("Введите последовательность чисел, разделяя их пробелом: ").split()))
lst = [randint(-100, 100) for i in range(15)]
print(lst)
heapsort(lst)
print(f"Отсортированный список: {lst}, результат сортировки - {lst == sorted(lst)}")

# Сложность: O(n * log(n)) в любом случае