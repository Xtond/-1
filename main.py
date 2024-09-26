import random #добавляем библиотеку рандома
import time #добавляем библиотеку для работы со временем

def generate_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def bubble_sort(arr):  #функция сортировки пузырьком
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
    return count

def insertion_sort(arr):  #функция сортировки вставками
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count += 1
        arr[j + 1] = key
    return count

def selection_sort(arr): #функция выборочной сортировки
    count = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if i != min_idx:
            count += 1
    return count

def quick_sort(arr): #функция быстрой сортировки
    if len(arr) <= 1:
        return arr, 0
    else:
        count = 0
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        count += len(arr) - 1  # учитываем все перестановки
        sorted_less, less_count = quick_sort(less)
        sorted_greater, greater_count = quick_sort(greater)
        count += less_count + greater_count
        return sorted_less + [pivot] + sorted_greater, count

def merge_sort(arr): #функция сортировки слиянием
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_sorted, left_count = merge_sort(left_half)
        right_sorted, right_count = merge_sort(right_half)

        i = j = k = 0
        count = left_count + right_count

        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                arr[k] = left_sorted[i]
                i += 1
            else:
                arr[k] = right_sorted[j]
                j += 1
            k += 1
            count += 1

        while i < len(left_sorted):
            arr[k] = left_sorted[i]
            i += 1
            k += 1
            count += 1

        while j < len(right_sorted):
            arr[k] = right_sorted[j]
            j += 1
            k += 1
            count += 1

        return arr, count
    else:
        return arr, 0

def shaker_sort(arr): #функция сортировки шейкером
    count = 0
    left = 0
    right = len(arr) - 1

    while left < right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
        right -= 1
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                count += 1
        left += 1
    return count

def sort_and_time(sort_func, arr): #функция которая отображает время сортировки и количество перестановок
    start_time = time.time()
    arr_copy = arr.copy()
    if sort_func in (quick_sort, merge_sort):
        sorted_arr, count = sort_func(arr_copy)
    else:
        count = sort_func(arr_copy)
        sorted_arr = arr_copy
    elapsed_time = time.time() - start_time
    return elapsed_time, count, sorted_arr

if __name__ == "__main__":
    size = int(input("Введите размер массива: "))
    random_array = generate_array(size)
    print("Исходный массив:", random_array)

    sorting_functions = {
        "Пузырьковая сортировка": bubble_sort,
        "Сортировка вставкой": insertion_sort,
        "Сортировка выбором": selection_sort,
        "Быстрая сортировка": quick_sort,
        "Сортировка слиянием": merge_sort,
        "Шейкерная сортировка": shaker_sort
    }

    for name, func in sorting_functions.items():
        if func in (quick_sort, merge_sort):
            elapsed_time, count, sorted_array = sort_and_time(func, random_array)
        else:

            elapsed_time, count, sorted_array = sort_and_time(func, random_array.copy())
        print(f"{name} - Время: {elapsed_time:.6f} сек, Перестановки: {count}, Результат: {sorted_array}")
