def swap_sort(lst):
    sorted_list = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if int(lst[j]) < int(lst[i]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst

lst = list(input("Введите последовательность чисел, разделяя их пробелом: ").split())
print(f"Отсортированный список: {swap_sort(lst)}")