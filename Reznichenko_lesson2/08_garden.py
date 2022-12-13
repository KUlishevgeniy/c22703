#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)
# выведите на консоль все виды цветов
all = garden_set | meadow_set
for i in all:
    print(i)
print()

# выведите на консоль те, которые растут и там и там
double = garden_set & meadow_set
for i in double:
    print(i)
print()
# выведите на консоль те, которые растут в саду, но не растут на лугу

garden = garden_set - meadow_set
for i in garden:
    print(i)
print()
# выведите на консоль те, которые растут на лугу, но не растут в саду

meadow = meadow_set - garden_set
for i in meadow:
    print(i)
print()
