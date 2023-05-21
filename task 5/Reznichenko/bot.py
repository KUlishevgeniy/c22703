import telebot
import psycopg2



bot = telebot.TeleBot('5869669112:AAFRWYzNfL9HJqHVf8FBoR5M8H5E3hNgTGQ')


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет, скажи мне id картины, о которой ты хотел бы узнать. Выбирай от 1 до 19")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        conn = psycopg2.connect(dbname='db', user='postgres', password='Q1w2e3r4', host='localhost')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM public.pictures WHERE id = {int(message.text)}")
        record = cursor.fetchall()
        conn.close()
        bot.send_message(message.from_user.id,
            f"""Название: {record[0][1]}\n\nАвтор: {record[0][2]}\n\nГод написания: {record[0][3]}\n\nОписание: {record[0][4]}""")
    except IndexError:
        bot.send_message(message.from_user.id, 'Вы ввели неверный id, введите число из промежутка 1-19')
    except ValueError:
        bot.send_message(message.from_user.id, 'Неверный формат данных, введите число из промежутка 1-19')


bot.infinity_polling()