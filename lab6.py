from random import randint
def selection_sort(arr):
    for i in range(len(arr)):
        min_element = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < min_element:
                min_element = arr[j]
                min_element_index = arr.index(arr[j])
        if arr[i] != min_element:
            arr[i], arr[min_element_index] = arr[min_element_index], arr[i]


#lst = list(map(int, input("Введите последовательность чисел, разделяя их пробелом: ").split()))
lst = [randint(-100, 100) for _ in range(14)]
print(lst)
selection_sort(lst)
print(f"Отсортированный список: {lst}, результат сортировки - {lst == sorted(lst)}")
# Сложность: O(n^2) в любом случае
