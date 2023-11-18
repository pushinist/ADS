from random import randint
def counting_sort(arr, place):
    output = [0] * len(arr)
    count = [0] * 10
    for i in range(len(arr)):
        index = arr[i] // place
        count[index % 10] += 1
    for i in range(len(count) - 1):
        count[i + 1] += count[i]
    i = len(arr) - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    max_el = max(arr)
    place = 1
    while max_el // place > 0:
        counting_sort(arr, place)
        place *= 10


#lst = list(map(int, input("Введите последовательность чисел, разделяя их пробелом: ").split()))
lst = [randint(-10000, 10000) for i in range(10)]
print(lst)
#lst = [48, 91, 9, 102]
arr_positive = [i for i in lst if i >= 0]
arr_negative = [abs(i) for i in lst if i < 0]
radix_sort(arr_positive)
if arr_negative:
    radix_sort(arr_negative)
arr_negative = [-1 * i for i in arr_negative]
arr_negative.reverse()
for i in arr_positive:
    arr_negative.append(i)
print(f"Отсортированный список: {arr_negative}, результат сортировки - {arr_negative == sorted(lst)}")
# Сложность: O(n) в любом случае