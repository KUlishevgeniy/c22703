#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append("Я")
my_family.append("Мама")
my_family.append("Папа")
my_family.append("Брат")
print(my_family)
# список списков приблизительного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [],
]
my_family_height.append(["Я",185])
my_family_height.append(["Лилия",160])
my_family_height.append(["Вадим",180])
my_family_height.append(["Амаль",110])
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост отца - ", my_family_height[3][1], " см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print("Общий рост моей семьи - ", my_family_height[1][1]+my_family_height[2][1]+my_family_height[3][1]+my_family_height[4][1], " см")