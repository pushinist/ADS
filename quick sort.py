import random
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    elem = lst[0]
    left = list(filter(lambda x: x < elem, lst))
    center = [i for i in lst if i == elem]
    right = list(filter(lambda x: x > elem, lst))

    return quick_sort(left) + center + quick_sort(right)

test_list = [random.randint(-100, 100) for i in range(15)]
print(test_list)
print(quick_sort(test_list))
print(quick_sort(test_list) == sorted(test_list))

# Сложность: O(n * log(n)) в лучшем случае, O(n^2) в худшем случае