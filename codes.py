#блочная сортировка
import random

def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    bucket_count = 10
    min_value = min(arr)
    max_value = max(arr)
    buckets = [[] for _ in range(bucket_count)]
    
    # Распределяем элементы по корзинам
    for num in arr:
        index = int((num - min_value) / (max_value - min_value + 1e-9) * bucket_count)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)
    
    # Сортируем каждую корзину и объединяем
    result = []
    for bucket in buckets:
        result += sorted(bucket)
    return result

# Генерация входных данных: 20 случайных чисел в диапазоне [0, 1)
data = [random.random() for _ in range(20)]
print("Входные данные:", data)

# Сортировка и вывод результата
sorted_data = bucket_sort(data)
print("Отсортированные данные:", sorted_data)


#блинная сортировка
import random

def flip(arr, k):
    # Переворачиваем первые k элементов массива
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1

def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        # Находим индекс максимального элемента в неотсортированной части
        mi = arr.index(max(arr[:curr_size]))
        # Если максимальный элемент не в правильной позиции, переворачиваем
        if mi != curr_size - 1:
            flip(arr, mi)
            flip(arr, curr_size - 1)
    return arr

# Генерация входных данных: 15 случайных целых чисел от 1 до 100
pancake_data = [random.randint(1, 100) for _ in range(15)]
print("Входные данные для блинной сортировки:", pancake_data)

# Сортировка и вывод результата
sorted_pancake = pancake_sort(pancake_data.copy())
print("Отсортированные данные блинной сортировкой:", sorted_pancake)




#Сортировка бусинами(гравитационная)
import numpy as np
import random

def bead_sort(arr):
    if any(type(x) != int or x < 0 for x in arr):
        raise ValueError("Bead sort работает только с неотрицательными целыми числами")
    max_elem = max(arr)
    beads = np.zeros((len(arr), max_elem), dtype=bool)
    for i, val in enumerate(arr):
        beads[i, :val] = True
    for j in range(max_elem):
        sum_ = beads[:, j].sum()
        beads[:, j] = False
        beads[-sum_:, j] = True
    for i in range(len(arr)):
        arr[i] = beads[i].sum()
    return arr

# Генерация входных данных: 15 случайных неотрицательных целых чисел от 0 до 50
bead_data = [random.randint(0, 50) for _ in range(15)]
print("Входные данные для сортировки бусинами:", bead_data)

# Сортировка и вывод результата
sorted_bead = bead_sort(bead_data.copy())
print("Отсортированные данные бусинами сортировкой:", sorted_bead)

#Поиск скачками
import math
def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))  # размер прыжка
    prev = 0
    # Алгоритм прыгает вперёд на m элементов, пока не найдёт элемент, больше или равный искомому
    while prev < n and arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    # Если найденный элемент больше искомого, выполняется линейный поиск в предыдущем блоке
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i
    return -1



#Экспоненциальный поиск
def exponential_search(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == x:
        return 0
    # Находим диапазон, где может находиться элемент
    i = 1
    while i < n and arr[i] <= x:
        i *= 2
    # Если элемент не найден, диапазон увеличивается экспоненциально: 1, 2, 4, 8, 16 и т.д., пока не будет найден элемент, больше или равный искомому
    left = i // 2
    right = min(i, n-1)
    return binary_search(arr, x, left, right)
def binary_search(arr, x, left, right): #На найденном диапазоне выполняется бинарный поиск
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1



#Тернарный поиск
def ternary_search(arr, x, left, right):
    if right >= left:
        # Делим массив на три части
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        #Сравнивается искомый элемент с элементами на двух разделительных границах
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        #Если совпадение не найдено, алгоритм повторяется рекурсивно в одной из трети массива, где может находиться искомое значение
        if x < arr[mid1]:
            return ternary_search(arr, x, left, mid1 - 1)
        elif x > arr[mid2]:
            return ternary_search(arr, x, mid2 + 1, right)
        else:
            return ternary_search(arr, x, mid1 + 1, mid2 - 1)
    return -1




