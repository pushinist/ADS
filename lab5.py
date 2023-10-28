def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

    
lst = list(map(int, input("Введите последовательность чисел, разделяя их пробелом: ").split()))
insertion_sort(lst)
print(f"Отсортированный список: {lst}, результат сортировки - {lst == sorted(lst)}")
