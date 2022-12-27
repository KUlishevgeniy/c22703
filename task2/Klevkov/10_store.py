#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
stol_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']+store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
divan_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']+store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
stul_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']+store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']+store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']

lamps_kolvo = store[goods['Лампа']][0]['quantity']
stol_kolvo = store[goods['Стол']][0]['quantity']+store[goods['Стол']][1]['quantity']
divan_kolvo = store[goods['Диван']][0]['quantity']+store[goods['Диван']][1]['quantity']
stul_kolvo = store[goods['Стул']][0]['quantity']+store[goods['Стул']][1]['quantity']+store[goods['Стул']][2]['quantity']


print('Лампы - ',lamps_kolvo, "шт, стоимость ", lamps_cost, 'руб.')
print('Столы - ',stol_kolvo, "шт, стоимость ", stol_cost, 'руб.')
print('Диваны - ',divan_kolvo, "шт, стоимость ", divan_cost, 'руб.')
print('Стулья - ',stul_kolvo, "шт, стоимость ", stul_cost, 'руб.')


# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.









