from random import randint


def heapify(array: list, length: int, root: int) -> None:
    largest = root  # Initialize largest as root
    left = 2 * root + 1  # left = 2*i + 1
    right = 2 * root + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root

    if left < length and array[root] < array[left]:
        largest = left

    # See if right child of root exists and is
    # greater than root

    if right < length and array[largest] < array[right]:
        largest = right

    # Change root, if needed

    if largest != root:
        (array[root], array[largest]) = (array[largest], array[root])  # swap

        # Heapify the root.

        heapify(array, length, largest)


# The main function to sort an array of given size

def heap_sort(array: list):
    length = len(array)

    # Build a maxheap.
    # Since last parent will be at ((length//2)-1) we can start at that location.

    for i in range(length // 2 - 1, -1, -1):
        heapify(array, length, i)

    for i in range(length - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])
        heapify(array, i, 0)
    return array


while True:
    n = input("Рандомный список (1) или выбранный (2) ? ")
    if n == '1':
        array = [randint(-1000, 1000) for i in range(5)]
        print(f"Сгенерированный список: {array}")
        break
    if n == '2':
        array = list(map(int, input().split()))
        break

sorted_array = heap_sort(array)
n = len(array)
print(f"Отсортированный список: {sorted_array}, результат сортировки: {array == sorted_array}")
