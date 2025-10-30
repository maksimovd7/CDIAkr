#блочная сортировка
def bucket_sort(arr): #Определяется количество корзин
    if len(arr) == 0:
        return arr
    bucket_count = 10
    min_value = min(arr)
    max_value = max(arr)
    buckets = [[] for _ in range(bucket_count)]
    # Каждый элемент помещается в корзину согласно функции распределения
    for i in arr:
        index = int((i - min_value) / (max_value - min_value + 1) * bucket_count)
        buckets[index].append(i)
    # Содержимое каждой корзины сортируется индивидуально
    result = []
    for bucket in buckets: #Корзины соединяются в порядке увеличения диапазона
        result += sorted(bucket)
    return result


#блинная сортировка
def flip(arr, k):
    #Переворачиваем подмассив от начала до позиции максимального элемента, чтобы этот элемент оказался первым
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1
def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        mi = arr.index(max(arr[:curr_size]))
        # Переворачиваем весь подмассив, чтобы максимальный элемент оказался в конце
        if mi != curr_size-1:#Повторяем процесс для оставшейся неотсортированной части массива
            flip(arr, mi)
            flip(arr, curr_size-1)
    return arr



#Сортировка бусинами(гравитационная)
def bead_sort(arr): #Каждый элемент массива представляется в виде горизонтального ряда бусин, количество которых соответствует его значению
    import numpy as np
    if any(type(x) != int or x < 0 for x in arr):
        raise ValueError("Bead sort работает только с неотрицательными целыми числами")
    max_elem = max(arr)
    beads = np.zeros((len(arr), max_elem), dtype=bool) #Бусины располагаются на «стержнях»
    for i, val in enumerate(arr):
        beads[i, :val] = True
    for j in range(max_elem): #Под действием «гравитации» бусины падают вниз
        sum_ = beads[:, j].sum()
        beads[:, j] = False
        beads[-sum_:, j] = True
    for i in range(len(arr)): #После оседания бусин строки считываются сверху вниз — получается отсортированный массив
        arr[i] = beads[i].sum()
    return arr



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




