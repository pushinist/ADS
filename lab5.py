def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp




    
arr = [int(x) for x in input("Введите набор чисел, разделяя их пробелом: ").split()]
insertion_sort(arr)
print(f"Отсортированный список: {arr}")
