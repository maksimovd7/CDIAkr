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
