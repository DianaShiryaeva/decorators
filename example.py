#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def decorator_strawberry(func):
    def wrapper():
        print('Клубника')
        func()
    return wrapper

def decorator_chocolate(func):
    def wrapper():
        print('Шоколадный сироп')
        func()
    return wrapper

def ice_cream_recipe():
    print('Мороженое')

while True:
    try:
        print('Здравствуйте! Какое мороженое желаете?\n 1. Обычное\n 2. С клубникой\n 3. С шоколадным сиропом\n 4. С клубникой и шоколадным сиропом')
        n = int(input("Введите только цифру: "))
        print()
        print("!!! Рецепт вашего мороженого:")
        match n:
            case 1:
                ice_cream_recipe()
            case 2:
                decorator_strawberry(ice_cream_recipe)()
            case 3:
                decorator_chocolate(ice_cream_recipe)()
            case 4:
                decorator_strawberry(decorator_chocolate(ice_cream_recipe))()
    except KeyboardInterrupt:
        print("\nПриятного аппетита")
        break