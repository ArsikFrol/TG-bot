import telebot
from telebot import types

bot = telebot.TeleBot('7839294840:AAHecX3AIO8LXSPA-UkynrFqHQziCgmffFs')

result_2_test = 0

listDDO = {
    "ddo_p": 0,
    "ddo_t": 0,
    "ddo_ch": 0,
    "ddo_z": 0,
    "ddo_x": 0,
}

direction = {
    "direction_a": 0,
    "direction_b": 0,
    "direction_c": 0
}

answersBasedOn3Tests = []


markup_items_temp = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
item_fleg = types.InlineKeyboardButton(text='Флегматик')
item_mel = types.InlineKeyboardButton(text='Меланхолик')
item_sang = types.InlineKeyboardButton(text='Сангвиник ')
item_hol = types.InlineKeyboardButton(text='Холерик')
markup_items_temp.add(item_fleg, item_mel, item_sang, item_hol)

markup_items_false_true = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
item_true = types.InlineKeyboardButton(text='Да 🔥')
item_false = types.InlineKeyboardButton(text='Нет ❌')
markup_items_false_true.add(item_true, item_false)