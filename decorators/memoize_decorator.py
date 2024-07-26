"""
    Этот декоратор полезен для оптимизации производительности рекурсивных или наиболее затратных функций, 
    поскольку он кэширует результаты предыдущих вызовов и возвращает их, если те же аргументы передаются снова.
"""

from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@memoize
def fibonacci(n):
    """Вернет n-е число Фибоначчи"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))