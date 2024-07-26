#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def decorator(func):
    '''Основная функция'''
    def wrapper(name):
        if name == "Котик":
            print("Вам можно")
        else:
            func()
    return wrapper

@decorator
def wrapped():
    print('Доступ запрещен всем!!!!!')

name = input("Ваше имя: ")
wrapped(name)
print('- конец программы')