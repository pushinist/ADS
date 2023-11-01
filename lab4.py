def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


lst = list(map(int, input("Введите последовательность чисел, разделяя их пробелом: ").split()))
bubble_sort(lst)
print(f"Отсортированный список: {lst}, результат сортировки по убыванию - {lst == list(reversed(sorted(lst)))}, по "
      f"возрастанию - {lst == sorted(lst)}")