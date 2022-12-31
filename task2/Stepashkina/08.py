#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',)

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',)

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =

garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
all_flowers = garden_set | meadow_set
print(*all_flowers)

# выведите на консоль те, которые растут и там и там
garden_and_meadow_flowers = garden_set & meadow_set
print(*garden_and_meadow_flowers)

# выведите на консоль те, которые растут в саду, но не растут на лугу
garden_flowers = all_flowers - meadow_set
print(*garden_flowers)

# выведите на консоль те, которые растут на лугу, но не растут в саду
meadow_flowers = all_flowers - garden_set
print(*meadow_flowers)
