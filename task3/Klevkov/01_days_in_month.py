# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if month <= 0 or month > 12:
    print('Месяца с таким номером не существует')
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print('В этом месяце 31 день')
elif month in [4, 6, 9, 11]:
    print('В этом месяцк 30 дней')
else:
    print('В этом месяце 28 дней')