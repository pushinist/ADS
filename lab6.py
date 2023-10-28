def selection_sort(arr):
    for i in range(len(arr)):
        min_element = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < min_element:
                min_element = arr[j]
                min_element_index = arr.index(arr[j])
        if arr[i] != min_element:
            arr[i], arr[min_element_index] = arr[min_element_index], arr[i]
    return arr


lst = list(map(int, input("Введите последовательность чисел, разделяя их пробелом: ").split()))
selection_sort(lst)
print(f"Отсортированный список: {lst}, результат сортировки - {lst == sorted(lst)}")


