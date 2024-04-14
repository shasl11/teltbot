import telebot
from telebot import types

bot = telebot.TeleBot('6469906732:AAEQgI740PgKXriIEUVPLNEcrvOgrC_N9JM')



@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Район', callback_data='rayon'))
    markup.add(types.InlineKeyboardButton('Количество гостей', callback_data='gosti'))
    markup.add(types.InlineKeyboardButton('Количество комнат', callback_data='room'))
    bot.send_message(message.chat.id, f'Здравствуйте, я помогу вам подобрать квартиру по вашим требованиям, {message.from_user.first_name}{message.from_user.last_name}')
    bot.send_message(message.chat.id,f'Какой параметр для вас наиболее важный?',reply_markup=markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Район', callback_data='rayon'))
    markup.add(types.InlineKeyboardButton('Количество гостей', callback_data='gosti'))
    markup.add(types.InlineKeyboardButton('Количество комнат', callback_data='room'))
    if callback.data == 'rayon':
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton('Индустриальный', callback_data='industrial'))
        markup1.add(types.InlineKeyboardButton('Центральный', callback_data='centr'))
        markup1.add(types.InlineKeyboardButton('Октябрьский', callback_data='october'))
        bot.send_message(callback.message.chat.id,f'Выберите район',reply_markup=markup1)
    elif callback.data == 'gosti':
        markup2 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('до 2-х', callback_data='2-h')
        btn2 = types.InlineKeyboardButton('до 3-х', callback_data='3-h')
        markup2.row(btn1,btn2)
        btn3 = types.InlineKeyboardButton('до 4-х', callback_data='4-h')
        btn4 = types.InlineKeyboardButton('до 6-ти', callback_data='6-h')
        markup2.row(btn3, btn4)
        bot.send_message(callback.message.chat.id, f'Выберите количество гостей', reply_markup=markup2)
    elif callback.data == 'room':
        markup3 = types.InlineKeyboardMarkup()
        markup3.add(types.InlineKeyboardButton('1', callback_data='one'))
        markup3.add(types.InlineKeyboardButton('2', callback_data='two'))
        markup3.add(types.InlineKeyboardButton('3', callback_data='three'))
        bot.send_message(callback.message.chat.id, f'Выберите количество комнат', reply_markup=markup3)

    elif callback.data == 'industrial':
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/47')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/48')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/51')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/52')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/54')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/49')
        bot.send_message(callback.message.chat.id, f'Подобрать по другим критериям?', reply_markup=markup)
    elif callback.data == 'october':
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/44')
        bot.send_message(callback.message.chat.id, f'Подобрать по другим критериям?', reply_markup=markup)
    elif callback.data == 'centr':
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/45')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/46')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/53')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/55')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/56')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/57')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/58')
        bot.send_message(callback.message.chat.id, f'Подобрать по другим критериям?',reply_markup=markup)


    elif callback.data == '2-h':
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/52')
        bot.send_message(callback.message.chat.id, f'Подобрать по другим критериям?', reply_markup=markup)
    elif callback.data == '3-h':
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/45')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/47')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/49')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/56')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/58')
        bot.send_message(callback.message.chat.id, f'Подобрать по другим критериям?',reply_markup = markup)
    elif callback.data == '4-h':
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/44')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/46')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/48')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/51')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/54')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/55')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/57')
        bot.send_message(callback.message.chat.id, f'Подобрать по другим критериям?', reply_markup=markup)
    elif callback.data == '6-h':
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/53')
        bot.send_message(callback.message.chat.id, f'Подобрать по другим критериям?', reply_markup=markup)


    elif callback.data == 'one':
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/47')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/48')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/49')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/51')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/52')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/55')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/56')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/57')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/58')
        bot.send_message(callback.message.chat.id, f'Подобрать по другим критериям?', reply_markup=markup)
    elif callback.data == 'two':
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/44')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/45')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/46')
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/54')
        bot.send_message(callback.message.chat.id, f'Подобрать по другим критериям?', reply_markup=markup)
    elif callback.data == 'three':
        bot.send_message(callback.message.chat.id, f'https://t.me/worldcapitalbarnaul/53')
        bot.send_message(callback.message.chat.id, f'Подобрать по другим критериям?', reply_markup=markup)












@bot.message_handler()
def chat(message):
    if message.text.lower() == 'привет':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Район', callback_data='rayon'))
        markup.add(types.InlineKeyboardButton('Количество гостей', callback_data='gosti'))
        markup.add(types.InlineKeyboardButton('Количество комнат', callback_data='room'))
        bot.send_message(message.chat.id,f'Здравствуйте, я помогу вам подобрать квартиру по вашим требованиям, {message.from_user.first_name}{message.from_user.last_name}')
        bot.send_message(message.chat.id, f'Какой параметр для вас наиболее важный?',reply_markup=markup)
    if message.text.lower() == 'старт':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Район', callback_data='rayon'))
        markup.add(types.InlineKeyboardButton('Количество гостей', callback_data='gosti'))
        markup.add(types.InlineKeyboardButton('Количество комнат', callback_data='room'))
        bot.send_message(message.chat.id,f'Здравствуйте, я помогу вам подобрать квартиру по вашим требованиям, {message.from_user.first_name}{message.from_user.last_name}')
        bot.send_message(message.chat.id, f'Какой параметр для вас наиболее важный?',reply_markup=markup)

bot.polling(none_stop=True)