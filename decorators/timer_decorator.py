#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from functools import wraps # используется декоратор functools.wraps для сохранения имени и строки документации (docstring) исходной функции

def timer(func):
    '''Измеряет длительность исполнения передаваемой функции'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start} seconds")
        return result
    return wrapper

@timer
def sort_bubble(array):
    """
    Алгоритм сортировки пузырьком
    """
    for i in range(len(array)-1):     # N-1 итераций работы алгоритма
        for j in range(0, len(array)-1-i):   # проход по оставшимся не отсортированным парам массива
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

@timer
def hello(name, target):
    """
    Алгоритм hello
    """
    print(f"Hello, {name} "*target)

arr = [100, 5, 45, 5, 76, 5, 2, 9, 3454, 7, 14, 16, 3, 56, 1, 76, 12, 4, 5, 2, 9, 34, 68, 21, 98, 86, 32, 8, 4, 2, 1, 5, 7, 1, 324, 31, 1, 43, 1, 34, 3, 435]*20

hello("Sem", 50)
sort_bubble(arr)