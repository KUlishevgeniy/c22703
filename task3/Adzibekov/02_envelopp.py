# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
if (envelop_x >= paper_x and envelop_y >= paper_y) or (envelop_x >= paper_y and envelop_y >= paper_x):
    print('ДА')
else:
    print('НЕТ')
# проверить для
paper_x, paper_y = 9, 8
if (envelop_x >= paper_x and envelop_y >= paper_y) or (envelop_x >= paper_y and envelop_y >= paper_x):
    print('ДА')
else:
    print('НЕТ')
    
paper_x, paper_y = 6, 8
if (envelop_x >= paper_x and envelop_y >= paper_y) or (envelop_x >= paper_y and envelop_y >= paper_x):
    print('ДА')
else:
    print('НЕТ')
    
paper_x, paper_y = 8, 6
if (envelop_x >= paper_x and envelop_y >= paper_y) or (envelop_x >= paper_y and envelop_y >= paper_x):
    print('ДА')
else:
    print('НЕТ')
    
paper_x, paper_y = 3, 4
if (envelop_x >= paper_x and envelop_y >= paper_y) or (envelop_x >= paper_y and envelop_y >= paper_x):
    print('ДА')
else:
    print('НЕТ')
    
paper_x, paper_y = 11, 9
if (envelop_x >= paper_x and envelop_y >= paper_y) or (envelop_x >= paper_y and envelop_y >= paper_x):
    print('ДА')
else:
    print('НЕТ')
    
paper_x, paper_y = 9, 11
if (envelop_x >= paper_x and envelop_y >= paper_y) or (envelop_x >= paper_y and envelop_y >= paper_x):
    print('ДА')
else:
    print('НЕТ')
