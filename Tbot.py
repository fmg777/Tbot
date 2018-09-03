import telebot
import urllib.request
import json
import random

from telebot import types

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

token = ""
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start', '/ttr', '/ico', '/rebus', '/kosti')
    user_markup.row('/eth', '/btc', '/pogoda', '/get_last_new')
    bot.send_message(message.from_user.id, 'Welcome back', reply_markup=user_markup)


# --------------------------------------------ETH
@bot.message_handler(commands=['eth'])  # моудль катировки эфира
def catirovkaETH(message):
    caterovka1 = urllib.request.urlopen(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD").read()

    jsonData = json.loads(caterovka1.decode())
    priceEthUsd = jsonData['RAW']['ETH']['USD']['PRICE']

    bot.reply_to(message, str(priceEthUsd) + "USD")


# -------------------------------------------BTC
@bot.message_handler(commands=['btc'])  # модуль катировки BTC
def catirovkaBTC(message):
    caterovka2 = urllib.request.urlopen(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD&e=Coinbase&extraParams=your_app_name").read()

    jsonData = json.loads(caterovka2.decode())
    priceBtcUSD = jsonData['RAW']['BTC']['USD']['PRICE']

    bot.reply_to(message, str(priceBtcUSD) + "USD")


# ----------------------------------------------------------Погода
@bot.message_handler(commands=['pogoda'])
def functiom(message):
    pogoda = urllib.request.urlopen(
        "http://api.openweathermap.org/data/2.5/weather?q=Balashikha,ru&APPID=640652626d5409d000c762be1168ee24").read()

    data = json.loads(pogoda.decode())
    tekpogoda = data['main']['temp']
    bot.reply_to(message, round(tekpogoda - 273))


# -----------------------------------------------news
@bot.message_handler(commands=['last_new'])
def function(message):
    news = urllib.request.urlopen('https://ttrcoin.com/article/novosti.12/').read()
    parsed_html = BeautifulSoup(news)
    links = parsed_html.find_all('a', attrs={'class': 'attachHolder'})
    bot.reply_to(message, "https://ttrcoin.com/article/novosti.12/" + links[1].get('href'))


# --------------------ИСО Предстаящие------------------------------------------

@bot.message_handler(commands=['ico'])
def function2(message):
    news2 = urllib.request.urlopen('https://ttrcoin.com/ico/').read()
    parsed_html2 = BeautifulSoup(news2)
    links1 = parsed_html2.find_all('a', attrs={'class': 'ico-block'})
    bot.reply_to(message, "https://ttrcoin.com/ico/" + links1[0].get('href'))


# Game KOSTI


igrok = random.randrange(1, 6 + 1)
komp = random.randrange(1, 6 + 1)
igrk1 = random.randrange(1, 6 + 1)
igrk2 = random.randrange(1, 6 + 1)
kompk1 = random.randrange(1, 6 + 1)
kompk2 = random.randrange(1, 6 + 1)
total_igr = igrk1 + igrk2
totalkomp = kompk1 + kompk2


@bot.message_handler(commands=['kosti'])
def startmessage(message: object):
    if message.text == '/kosti':
        bot.reply_to(message, "Готов играть?", reply_markup=inline_keyboard_kosti)


inline_keyboard_kosti = types.InlineKeyboardMarkup()
vopros1 = types.InlineKeyboardButton('Да', callback_data='otvet_da')
vopros1_1 = types.InlineKeyboardButton('Нет', callback_data='otvet_net')
inline_keyboard_kosti.add(vopros1, vopros1_1)

inline_keyboard_kosti2 = types.InlineKeyboardMarkup()
vopros2 = types.InlineKeyboardButton('Орел', callback_data='orel')
vopros2_2 = types.InlineKeyboardButton('Решка', callback_data='reshka')
inline_keyboard_kosti2.add(vopros2, vopros2_2)

inline_keyboard_kosti3 = types.InlineKeyboardMarkup()
vopros3 = types.InlineKeyboardButton('Бросить кости', callback_data='brosok')
inline_keyboard_kosti3.add(vopros3)

inline_keyboard_kosti4 = types.InlineKeyboardMarkup()
vopros4 = types.InlineKeyboardButton('Бросить кости', callback_data='brosok2')
inline_keyboard_kosti4.add(vopros4)

# Угадай слово

part1 = ("доктор", "стакан", "плед", "диван", "ковер", "карта")
part2 = ("кровля", "графин", "яблоня", "прыжок", "параграф", "подкова", "корабль", "дурман")
part3 = ("эпидемия", "революция", "серпантин", "эллюминатор", "коромысло", "стропила", "калейдоскоп", "буровзрывной")

# Уровень 1
round1 = random.choice(part1)

savetext_round1 = round1
sobiraem_slovo = " "

for i in range(len(savetext_round1)):
    random_letter = random.randrange(len(savetext_round1))
    sobiraem_slovo += savetext_round1[random_letter]
    savetext_round1 = (savetext_round1[:random_letter] + savetext_round1[(random_letter + 1):])

# Уровень 2

round2 = random.choice(part2)
save_text2 = round2
sobiraem_slovo2 = " "
for i in range(len(save_text2)):
    random_letter2 = random.randrange(len(save_text2))
    sobiraem_slovo2 += save_text2[random_letter2]
    save_text2 = (save_text2[:random_letter2] + save_text2[random_letter2 + 1:])

# Уровень 3

round3 = random.choice(part3)

save_text3 = round3
sobiraem_slovo3 = " "
for i in range(len(save_text3)):
    random_letter3 = random.randrange(len(save_text3))
    sobiraem_slovo3 += save_text3[random_letter3]
    save_text3 = (save_text3[:random_letter3] + save_text3[random_letter3 + 1:])


@bot.message_handler(commands=['rebus'])
def game_rebus(message: object):
    if '/rebus' == message.text:
        bot.reply_to(message, "Готов играть?", reply_markup=inline_rebus)


inline_rebus = types.InlineKeyboardMarkup()
rebus1 = types.InlineKeyboardButton('Да', callback_data='da')
rebus1_1 = types.InlineKeyboardButton('Нет', callback_data='net')
inline_rebus.add(rebus1, rebus1_1)

inline_rebus2 = types.InlineKeyboardMarkup()
rebus2 = types.InlineKeyboardButton('Уровень 1', callback_data='lvl1')
inline_rebus2.add(rebus2)

inline_rebus3 = types.InlineKeyboardMarkup()
rebus3 = types.InlineKeyboardButton('Уровень 2', callback_data='lvl2')
rebus3_1 = types.InlineKeyboardButton('Выход', callback_data='exit')
inline_rebus3.add(rebus3, rebus3_1)

inline_rebus4 = types.InlineKeyboardMarkup()
rebus4 = types.InlineKeyboardButton('Уровень 3', callback_data='lvl3')
rebus4_1 = types.InlineKeyboardButton('Выход', callback_data='exit2')
inline_rebus4.add(rebus4, rebus4_1)


@bot.callback_query_handler(func=lambda call: True)
def game_kosti(call):
    if call.data == 'otvet_da':
        bot.send_message(call.message.chat.id,
                         text="Тогда начнем.Определим кто будет ходить первым путем подкидывания монетки",
                         reply_markup=inline_keyboard_kosti2)
    if call.data == 'orel' or call.data == 'reshka':
        bot.send_message(call.message.chat.id, text="Проводим жеребьевку")
        if igrok < komp:
            bot.send_message(call.message.chat.id, text="Первым бросает кости компьютер")
            bot.send_message(call.message.chat.id,
                             text="Выпадает:" + str(kompk1) + " " + " и " + str(kompk2) + " " + "В сумме:" + str(
                                 totalkomp))
            bot.send_message(call.message.chat.id, text="Теперь твой черед", reply_markup=inline_keyboard_kosti3)
        if igrok >= komp:
            bot.send_message(call.message.chat.id, text="Ты начинай игру.Бросай кости",
                             reply_markup=inline_keyboard_kosti4)

    if call.data == 'brosok':
        bot.send_message(call.message.chat.id,
                         text="Выпадает: " + str(igrk1) + " " + " и " + str(igrk2) + " " + "В сумме:" + str(total_igr))
        if totalkomp > total_igr:
            bot.send_message(call.message.chat.id, text="Ты проиграл")
        elif totalkomp < total_igr:
            bot.send_message(call.message.chat.id, text="Ты выиграл")
        else:
            bot.send_message(call.message.chat.id, text="Ничья")

    if call.data == 'brosok2':
        bot.send_message(call.message.chat.id,
                         text="Выпадает: " + str(igrk1) + " " + " и " + str(igrk2) + " " + "В сумме:" + str(total_igr))
        bot.send_message(call.message.chat.id, text="Теперь бросает кости компьютер")
        bot.send_message(call.message.chat.id,
                         text="Выпадает:" + str(kompk1) + " " + " и " + str(kompk2) + " " + "В сумме:" + str(totalkomp))
        if totalkomp > total_igr:
            bot.send_message(call.message.chat.id, text="Ты проиграл")
        elif totalkomp < total_igr:
            bot.send_message(call.message.chat.id, text="Ты выиграл")
        else:
            bot.send_message(call.message.chat.id, text="Ничья")

    if call.data == 'otvet_net':
        bot.send_message(call.message.chat.id, text="Тогда в другой раз.Если что ты знаешь как меня найти.")

    # Ребус------------------------------------------------------------------------------------------------------

    if call.data == 'da':
        bot.send_message(call.message.chat.id, text="Правила", reply_markup=inline_rebus2)
    if call.data == 'lvl1':
        bot.send_message(call.message.chat.id, text="Расшифруй слово - :" + sobiraem_slovo)

    if call.data == 'lvl2':
        bot.send_message(call.message.chat.id, text="Расшифруй слово - " + sobiraem_slovo2)

    if call.data == 'lvl3':
        bot.send_message(call.message.chat.id, text="Финальное слово - " + sobiraem_slovo3)

    if call.data == 'exit':
        bot.send_message(call.message.chat.id, text="Спасибо за игру")

    if call.data == 'net':
        bot.send_message(call.message.chat.id, text="Тогда в другой раз.Если что ты знаешь как меня найти.")

    if call.data == 'exit2':
        bot.send_message(call.message.chat.id, text="Ты был в шаге от победы.Удачи")


# ----------------------------------------------------------------------------------------------------------------------

@bot.message_handler(content_types=['text'])
def sage1(message: object):
    if round1 in message.text:
        bot.reply_to(message, "Верно.Играем дальше?", reply_markup=inline_rebus3)
        return

    if round2 in message.text:
        bot.reply_to(message, "Верно.Играем дальше?", reply_markup=inline_rebus4)
        return

    if round3 in message.text:
        bot.reply_to(message, "Верно.Ты выиграл.Наши поздравления!!!")
        return


# ------------------------------------------------------------------------------------------------------------------------


bot.polling()
