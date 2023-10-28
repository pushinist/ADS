def shell_sort(arr):
    n = len(arr)
    t = n // 2
    while t > 0:
        for i in range(t, n):
            temp = i
            delta = temp - t
            while delta >= 0 and arr[delta] > arr[temp]:
                arr[delta], arr[temp] = arr[temp], arr[delta]
                temp = delta
                delta = temp - t
        t //= 2
    return arr


lst = list(map(int, input("Введите последовательность чисел, разделяя их пробелом: ").split()))
shell_sort(lst)
print(f"Отсортированный список: {lst}, результат сортировки - {lst == sorted(lst)}")