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
import random

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Находим блок, где может находиться элемент
    while prev < n and arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Линейный поиск в блоке
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i
    return -1

# Генерация тестовых данных: отсортированный список из 30 уникальных случайных чисел от 1 до 100
data = sorted(random.sample(range(1, 101), 30))
print("Отсортированные входные данные:", data)

# Элемент для поиска
target = data[random.randint(0, len(data)-1)]
print("Искомый элемент:", target)

# Запуск поиска
index = jump_search(data, target)
print(f"Элемент {target} найден на индексе:", index)



#Экспоненциальный поиск
def binary_search(arr, x, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, x):
    if len(arr) == 0:
        return -1
    if arr[0] == x:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= x:
        index *= 2
    return binary_search(arr, x, index // 2, min(index, len(arr) - 1))

# Входные данные: массив отсортированных чисел
data = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
# Искомый элемент
target = 128
print("Массив:", data)
print("Ищем:", target)

# Запуск алгоритма
result_index = exponential_search(data, target)
print("Индекс найденного элемента:", result_index)


#Тернарный поиск
import random

# Генерация тестовых данных: отсортированный список из 30 случайных чисел в диапазоне от -50 до 50
data = sorted([random.randint(-50, 50) for _ in range(30)])

print("Входные данные для тернарного поиска:", data)

# Для демонстрации поиска можно выбрать, например, индекс равный 0 или последний
target = data[0]
print("Ищем элемент:", target)

# Реализация тернарного поиска (поиск минимума на отсортированном массиве)
def ternary_search(arr, x):
    left, right = 0, len(arr) - 1
    while right - left > 2:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3
        if arr[m1] == x:
            return m1
        if arr[m2] == x:
            return m2
        if arr[m1] > x:
            right = m1 - 1
        elif arr[m2] < x:
            left = m2 + 1
        else:
            left = m1 + 1
            right = m2 - 1
    # Линейный поиск для оставшихся элементов
    for i in range(left, right + 1):
        if arr[i] == x:
            return i
    return -1

# Запускаем поиск
index_found = ternary_search(data, target)
print("Индекс найденного элемента:", index_found)




