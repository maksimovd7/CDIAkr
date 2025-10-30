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

