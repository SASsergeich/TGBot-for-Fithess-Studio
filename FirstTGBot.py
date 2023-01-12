import telebot
from telebot import types
from Config import API_KEY

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Да!💪')
    item2 = types.KeyboardButton('Конечно!👍')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Здравствуйте, хотите начать заниматься в лучшей фитнесс студии Краснодара?',
    reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answers(message):
    if message.text == 'Да!💪':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        day_1 = types.KeyboardButton('Понедельник')
        day_2 = types.KeyboardButton('Вторник')
        day_3 = types.KeyboardButton('Среда')
        day_4 = types.KeyboardButton('Четверг')
        day_5 = types.KeyboardButton('Пятница')
        day_6 = types.KeyboardButton('Суббота')
        day_7 = types.KeyboardButton('Воскресенье')
        markup.add(day_1, day_2, day_3, day_4, day_5, day_6, day_7)
        bot.send_message(message.chat.id, 'Отлично! В какой день недели вам будет удобно тренироваться?',
        reply_markup=markup)
    elif message.text == 'Конечно!👍':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        day_1 = types.KeyboardButton('Понедельник')
        day_2 = types.KeyboardButton('Вторник')
        day_3 = types.KeyboardButton('Среда')
        day_4 = types.KeyboardButton('Четверг')
        day_5 = types.KeyboardButton('Пятница')
        day_6 = types.KeyboardButton('Суббота')
        day_7 = types.KeyboardButton('Воскресенье')
        exite = types.KeyboardButton('Назад⬅')
        markup.add(day_1, day_2, day_3, day_4, day_5, day_6, day_7, exite)
        bot.send_message(message.chat.id, 'Отлично! В какой день недели вам будет удобно тренироваться?',
        reply_markup=markup)
    elif message.text == 'Понедельник':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        train_1 = types.KeyboardButton('Силовая тренировка в 10:00. Тренер - Алёна.')
        train_2 = types.KeyboardButton('Функциональная тренировка в 19:00. Тренер - Анна.')
        train_3 = types.KeyboardButton('Силовая тренировка в 20:00. Тренер - Анна.')
        exite = types.KeyboardButton('Назад⬅')
        markup.add(train_1, train_2, train_3, exite)
        bot.send_message(message.chat.id, 'Замечательно! Выберите время для тренировки:',
        reply_markup=markup)
    elif message.text == 'Вторник':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        train_1 = types.KeyboardButton('Силовая тренировка в 19:30. Тренер - Алексей.')
        train_2 = types.KeyboardButton('Функциональная тренировка в 20:30. Тренер - Алексей.')
        exite = types.KeyboardButton('Назад⬅')
        markup.add(train_1, train_2, exite)
        bot.send_message(message.chat.id, 'Замечательно! Выберите время для тренировки:',
        reply_markup=markup)
    elif message.text == 'Среда':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        train_1 = types.KeyboardButton('Силовая тренировка в 10:00. Тренер - Алексей.')
        train_2 = types.KeyboardButton('Функциональная тренировка в 19:00. Тренер - Алексей.')
        train_3 = types.KeyboardButton('Силовая тренировка в 20:00. Тренер - Анна.')
        exite = types.KeyboardButton('Назад⬅')
        markup.add(train_1, train_2, train_3, exite)
        bot.send_message(message.chat.id, 'Замечательно! Выберите время для тренировки:',
        reply_markup=markup)
    elif message.text == 'Четверг':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        train_1 = types.KeyboardButton('Функциональная тренировка в 19:30. Тренер - Анна.')
        train_2 = types.KeyboardButton('Силовая тренировка в 20:30. Тренер - Алексей.')
        exite = types.KeyboardButton('Назад⬅')
        markup.add(train_1, train_2, exite)
        bot.send_message(message.chat.id, 'Замечательно! Выберите время для тренировки:',
        reply_markup=markup)
    elif message.text == 'Пятница':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        train_1 = types.KeyboardButton('Растяжка в 10:00. Тренер - Алёна.')
        train_2 = types.KeyboardButton('Степ Аэробика в 18:00. Тренер - Анна.')
        train_3 = types.KeyboardButton('Силовая тренировка в 19:00. Тренер - Анна.')
        train_4 = types.KeyboardButton('Круговая тренировка в 20:00. Тренер - Алексей.')
        exite = types.KeyboardButton('Назад⬅')
        markup.add(train_1, train_2, train_3, train_4, exite)
        bot.send_message(message.chat.id, 'Замечательно! Выберите время для тренировки:',
        reply_markup=markup)
    elif message.text == 'Суббота':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        train_1 = types.KeyboardButton('МиоФасциальный релиз (МФР) в 10:00. Тренер - Анна.')
        exite = types.KeyboardButton('Назад⬅')
        markup.add(train_1, exite)
        bot.send_message(message.chat.id, 'Замечательно! Выберите время для тренировки:',
        reply_markup=markup)
    elif message.text == 'Воскресенье':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        train_1 = types.KeyboardButton('Функциональная тренировка в 10:00. Тренер - Анна.')
        train_2 = types.KeyboardButton('ZUMBA в 11:00. Тренер - Юлия.')
        train_3 = types.KeyboardButton('Силовая тренировка в 18:00. Тренер - Анна.')
        exite = types.KeyboardButton('Назад⬅')
        markup.add(train_1, train_2, train_3, exite)
        bot.send_message(message.chat.id, 'Замечательно! Выберите время для тренировки:',
        reply_markup=markup)
    elif message.text == 'Назад⬅':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        day_1 = types.KeyboardButton('Понедельник')
        day_2 = types.KeyboardButton('Вторник')
        day_3 = types.KeyboardButton('Среда')
        day_4 = types.KeyboardButton('Четверг')
        day_5 = types.KeyboardButton('Пятница')
        day_6 = types.KeyboardButton('Суббота')
        day_7 = types.KeyboardButton('Воскресенье')
        markup.add(day_1, day_2, day_3, day_4, day_5, day_6, day_7)
        bot.send_message(message.chat.id, 'Отлично! В какой день недели вам будет удобно тренироваться?',
        reply_markup=markup)
    elif message.text =='Силовая тренировка в 10:00. Тренер - Алёна.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Функциональная тренировка в 19:00. Тренер - Анна.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Силовая тренировка в 20:00. Тренер - Анна.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Силовая тренировка в 19:30. Тренер - Алексей.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Функциональная тренировка в 20:30. Тренер - Алексей.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Силовая тренировка в 10:00. Тренер - Алексей.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Функциональная тренировка в 19:00. Тренер - Алексей.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Силовая тренировка в 20:00. Тренер - Анна.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Функциональная тренировка в 19:30. Тренер - Анна.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Силовая тренировка в 20:30. Тренер - Алексей.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Растяжка в 10:00. Тренер - Алёна.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Степ Аэробика в 18:00. Тренер - Анна.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Силовая тренировка в 19:00. Тренер - Анна.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Круговая тренировка в 20:00. Тренер - Алексей.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='МиоФасциальный релиз (МФР) в 10:00. Тренер - Анна.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='ZUMBA в 11:00. Тренер - Юлия.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')
    elif message.text =='Силовая тренировка в 18:00. Тренер - Анна.':
        bot.send_message(message.chat.id, 'Для брони свяжитесь с тренером по номеру ..., Наш фитнесс зал находится по адресу ул.Командорская 3к2.Желаем вам продуктивных тренировок!')

    else:
        bot.send_message(message.chat.id, 'Лучше нажмите на одну из кнопок!')

bot.polling(none_stop=True)