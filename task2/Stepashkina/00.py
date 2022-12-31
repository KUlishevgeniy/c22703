#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

for i in sites:
    for j in sites:
        if i != j and ((j, i) not in distances):
            distances[(i, j)] = \
                ((sites[i][0] - sites[j][0]) ** 2 + (sites[i][1] - sites[j][1]) ** 2) ** 0.5

print(distances)
