import telebot
from telebot import types

import Variabelsbot as Var

import test1

@Var.bot.message_handler(commands=['start', 'help'])  # фукнция которая отвечает за старт бота
def start(message):
    msg = Var.bot.send_message(message.chat.id, f'Привет!Это профориентационный чат-бот «Твой выбор».Давай пройдем тест на темперамент ,т.к он формирует способы взаимодействия с окружающими и предпочтения в рабочей среде, что влияет на удовлетворённость от профессиональной деятельности?',
        reply_markup=Var.markup_items_false_true) 
    Var.bot.register_next_step_handler(msg, item_selection_check)

def item_selection_check(message):    # проверка ответа пользователя
    if message.text == 'Да 🔥':
        msg = Var.bot.send_message(message.chat.id, 'Любите ли вы ходить в гости?',
        reply_markup=Var.markup_items_false_true)
        Var.bot.register_next_step_handler(msg, test1.answer_2)
    else:
        msg = Var.bot.send_message(message.chat.id, 'ТОП - 10 профессий\n1)Инженер\n2)Финансовый аналитик\n3)Маркетолог\n4)IT-специалист\n5)учитель\n6)Психотерапевт, психолог\n7)Медицинский работник\n8)Специалист нефтегазовой отрасли\n9)специалисты в области современного сельского хозяйства\n10)Военнослужащие')

Var.bot.polling()