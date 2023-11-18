from random import randint

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

    
#lst = list(map(int, input("Введите последовательность чисел, разделяя их пробелом: ").split()))
lst = [randint(-100, 100) for _ in range(14)]
lst.append(0)
print(lst)
insertion_sort(lst)
print(f"Отсортированный список: {lst}, результат сортировки - {lst == sorted(lst)}")

# Сложность: O(n^2) в худшем случае, O(n) в лучшем случае