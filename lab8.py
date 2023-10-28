def counting_sort(arr, place):
    output = [0] * len(arr)
    count = [0] * (max(arr) + 1)
    for i in range(len(arr)):
        index = arr[i] // place
        count[index % 10] += 1
    for i in range(len(count) - 1):
        count[i + 1] += count[i]
    i = len(arr) - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    max_el = max(arr)
    place = 1
    while max_el // place > 0:
        counting_sort(arr, place)
        place *= 10


arr = [121, 432, 564, 23, 1, 45, 788]
radix_sort(arr)
print(arr)
