def swap_sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]


lst = list(map(int, input("Введите последовательность чисел, разделяя их пробелом: ").split()))
swap_sort(lst)
print(f"Отсортированный список: {lst}, результат сортировки - {lst == sorted(lst)}")