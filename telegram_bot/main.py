import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6808991384:AAHn6W08CQCVoGTmfCZMr3KMIgtSkeODt70')

marked_weekday = 5


@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://github.com/ugapanyuk/courses_content/wiki/COURSE_PCPL_2023')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,
                     'You can control me by sending these commands:\n/site - открыть страницу курса на github\n'
                     '/university_info - информация об университете\n'
                     '/teacher_info - информация о преподавателе\n'
                     '/schedule - расписание пар для групп')


@bot.message_handler(commands=['university_info'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://bmstu.ru/'))
    bot.send_message(message.chat.id, '<b>Московский государственный технический университет им. Н.Э. Баумана</b> '
                                      '— российский национальный исследовательский университет, научный центр и особо ценный объект культурного наследия народов России. '
                                      'Индикатор успеха — формирование в массовом сознании в России и за рубежом понятия или образа «русский инженер».',
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['teacher_info'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://iu5.bmstu.ru/user/profile.php?id=5'))
    bot.send_message(message.chat.id,
                     '<b>Гапанюк Юрий Евгеньевич</b> родился в 1974 году в г. Москве. В 1998 году окончил кафедру ИУ-5 МГТУ им. Н.Э.Баумана с отличием.'
                     'В 2006 году защитил в МГТУ им. Н.Э.Баумана кандидатскую диссертацию по специальности 05.13.17. '
                     'Работает на кафедре ИУ-5 с 1998 года в должности ассистента, доцента. Научные интересы: языки программирования, модели данных,'
                     ' интеллектуальные системы обработки информации, машинное обучение.', parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['schedule'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('ИУ5-31Б', callback_data='group_31B')
    btn2 = types.InlineKeyboardButton('ИУ5-32Б', callback_data='group_32B')
    btn3 = types.InlineKeyboardButton('ИУ5-33Б', callback_data='group_33B')
    btn4 = types.InlineKeyboardButton('ИУ5-34Б', callback_data='group_34B')
    btn5 = types.InlineKeyboardButton('ИУ5-35Б', callback_data='group_35B')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5)
    bot.send_message(message.chat.id, 'Выберите номер группы:', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'group_31B':
        bot.send_message(callback.message.chat.id, 'Числитель, понедельник, 12:00-13:35')
    if callback.data == 'group_32B':
        bot.send_message(callback.message.chat.id, 'Знаменатель, вторник, 15:40-17:15')
    if callback.data == 'group_33B':
        bot.send_message(callback.message.chat.id, 'Знаменатель, понедельник, 15:40-17:15')
    if callback.data == 'group_34B':
        bot.send_message(callback.message.chat.id, 'Числитель, понедельник, 15:40-17:15')
    if callback.data == 'group_35B':
        bot.send_message(callback.message.chat.id, 'Знаменатель, вторник, 13:50-15:25')


bot.polling(none_stop=True)
