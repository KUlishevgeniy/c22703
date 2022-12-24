#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append("МАМА")
my_family.append("ПАПА")
my_family.append("БРАТ")
print(my_family)
# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [],
]
my_family_height.append(["Наталья",175])
my_family_height.append(["Олег",183])
my_family_height.append(["Илья",193])
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост отца - ", my_family_height[2][1], " см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print("Общий росто моей семьи - ", my_family_height[1][1]+my_family_height[2][1]+my_family_height[3][1], " см")
