"""
    Этот декоратор полезен при отладке, поскольку он выводит (prints) имя, аргументы и возвращаемое значение оборачиваемой функции. 
    Он также использует декоратор functools.wraps для сохранения имени и docstring исходной функции.
"""

from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@debug
def add(x, y):
    """Вернет сумму х и у"""
    return x + y

@debug
def greet(name, message="Hello"):
    """Возвращает приветственное сообщение с именем"""
    return f"{message}, {name}!"

add(2, 3)
greet("Alice")
greet("Bob", message="Hi")