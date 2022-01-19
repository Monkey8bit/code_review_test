import cProfile
from timeit import timeit
from random import randint
from sys import getsizeof


# для сравнения возьмём функцию сортировки слиянием из предыдущей задачи
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = (len(nums) - 1) // 2
    lst1 = merge_sort(nums[:mid + 1])
    lst2 = merge_sort(nums[mid + 1:])
    result = merge(lst1, lst2)
    return result


def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while i <= len(lst1) - 1 and j <= len(lst2) - 1:
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    if i > len(lst1) - 1:
        while j <= len(lst2) - 1:
            lst.append(lst2[j])
            j += 1
    else:
        while i <= len(lst1) - 1:
            lst.append(lst1[i])
            i += 1
    return lst


# сравнивать будем с сортировкой пузырьком
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


rnd_lst = [randint(1, 100) for i in range(100)]


"""timeit - функция, выполняющая указанный код столько раз, сколько этого требует пользователь.
В данном случае, в зависимости от сложности алгоритма, сортировка займет разное время.
"""

print(timeit("bubble_sorted = bubble_sort(rnd_lst)", number=10000, globals=globals()))
print(timeit("merge_sorted = merge_sort(rnd_lst)", number=10000, globals=globals()))

"""
cProfile - модуль, позволяющий найти слабые места в коде.
"""

rnd_lst_2 = [randint(1, 10000) for n in range(10000)]
cProfile.run("bubble_sorted = bubble_sort(rnd_lst_2)")

"""
С помощью getsizeof() из модуля sys можно определить, сколько места в памяти занимает тот или иной объект."""

some_gen = (num for num in range(10000000))
some_lst = [num for num in range(10000000)]

print(f"Size of generator: {getsizeof(some_gen)}\nSize of list: {getsizeof(some_lst)}")

"""
В данном примере, генератор занимает в памяти гораздо меньше места, потому что не хранит все элементы 
последовательности в памяти, а отдает по необходимости через next() в итерации, либо вручную.
Однако, в отличии от списка, один раз отдав последовательность, генератор остается пустым без возможности 
повторно использовать его элементы в коде, пока не будет создан заново.
"""
