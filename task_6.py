"""Если я правильно понял задачу, то нужно реализовать бинарный поиск именно в случайном массиве,
т.е. сначала отсортировать его при необходимости.
"""

from random import randint


def merge_sort(nums):  # основная функция сортировки
    if len(nums) == 1:  # если в массиве один элемент - он уже отсортирован
        return nums
    mid = (len(nums) - 1) // 2  # находим середину массива
    lst1 = merge_sort(nums[:mid + 1])  # рекурсивно делим на две части
    lst2 = merge_sort(nums[mid + 1:])  # пока не останется один элемент в массиве
    result = merge(lst1, lst2)  # после поочередно склеиваем
    return result


def merge(lst1, lst2):
    lst = []  # массив для отсортированных частей двух списков
    i = 0
    j = 0
    while i <= len(lst1) - 1 and j <= len(lst2) - 1:
        if lst1[i] < lst2[j]:  # если число в первом списке меньше, чем число во втором,
            lst.append(lst1[i])  # сначала вставляем число из первого списка
            i += 1
        else:
            lst.append(lst2[j])  # иначе вставляем число из второго списка
            j += 1
    if i > len(lst1) - 1:  # итерируемся по оставшемуся списку с большей длиной
        while j <= len(lst2) - 1:
            lst.append(lst2[j])
            j += 1
    else:
        while i <= len(lst1) - 1:
            lst.append(lst1[i])
            i += 1
    return lst


def binary(num, arr, left, right):
    if right >= left:  # если правая граница больше левой границы, т.е. пока в списке есть хотя бы один элемент

        mid = (left + right) // 2  # находим середину списка
        if num == arr[mid]:  # если число найдено - возвращаем его индекс
            return f"Index of your number is: {mid}"
        elif num < arr[mid]:  # если число меньше - рекурсивно вызываем функцию для левой половины
            return binary(num, arr, left, mid - 1)
        elif num > arr[mid]:  # если больше - для правой
            return binary(num, arr, mid + 1, right)
    else:
        return f"Number {num} doesn't exist in array."  # если число не в списке


rand_lst = [randint(1, 100) for i in range(100)]
if rand_lst != sorted(rand_lst):  # проверка, отсортирован ли массив
    rand_lst = merge_sort(rand_lst)  # если нет - сортируем

number = randint(1, 100)
print(rand_lst)
if number in rand_lst:  # проверка, что функция отработает правильно
    print(f"{number} is in array, checking position..")
print(binary(number, rand_lst, 0, len(rand_lst) - 1))
