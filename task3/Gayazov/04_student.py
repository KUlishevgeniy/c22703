# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
yxoddeneg = 0
prixoddeneg = 0
month = 1
while month <= 10:
    prixoddeneg += educational_grant
    yxoddeneg += expenses
    expenses *= 1.03
    month += 1
shekeli = yxoddeneg - prixoddeneg
print("Студенту надо попросить", round(shekeli,2),"рублей")