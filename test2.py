import Variabelsbot as Var
from telebot import types

import test3

def answer_2(ms):   # функция отвечает за 2 вопрос второго теста

    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Управлять автомобилем, автобусом, самолетом, судном или другим транспортным средством')
    with open('./images/images2Test/2_2a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Корректировать фотоснимки с помощью компьютерных программ')
    with open('./images/images2Test/2_2b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'o':
        print('o')
        Var.listDDO['ddo_z'] += 1
    if ms.text == 'б':
        Var.listDDO['ddo_ch'] += 1

    Var.bot.register_next_step_handler(msg, answer_2)

def answer_3(ms):   # функция отвечает за 3 вопрос второго теста

    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Лечить кошек, собак, лошадей и других животных')
    with open('./images/images2Test/2_3a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Заниматься записью, воспроизведением, обработкой, компоновкой музыкальных композиций в звуковых студиях')
    with open('./images/images2Test/2_3b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_4)
    if ms.text == 'б':
       Var.listDDO['ddo_x'] += 1
       Var.bot.register_next_step_handler(msg, answer_4)

def answer_4(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Проводить финансовый анализ рынка ценных бумаг')
    msg = Var.bot.send_message(ms.chat.id, 'б)Исследовать работу мозга живых существ в специальной лаборатории')

    if ms.text == 'а':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_5)
    if ms.text == 'б':
        Var.listDDO['ddo_x'] += 1
        Var.bot.register_next_step_handler(msg, answer_5)

def answer_5(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Оказывать людям медицинскую или психологическую помощь')
    with open('./images/images2Test/2_5a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Налаживать работу компьютеров, оборудования')
    with open('./images/images2Test/2_5b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_6)
    if ms.text == 'б':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_6)

def answer_6(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Тестировать компьютеры перед их продажей')
    msg = Var.bot.send_message(ms.chat.id, 'б)Обрабатывать, анализировать и обобщать социологические данные')

    if ms.text == 'а':
        Var.listDDO['ddo_ch'] += 1
        Var.bot.register_next_step_handler(msg, answer_7)
    if ms.text == 'б':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_7)

def answer_7(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Быть журналистом и писать статьи, освещая происходящие события')
    with open('./images/images2Test/2_7a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Рассчитывать экономически выгодный путь транспортировки товара до потребителя')
    with open('./images/images2Test/2_7b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_8)
    if ms.text == 'б':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_8)

def answer_8(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Обеспечивать исправное состояние, безаварийную и надежную работу обслуживаемой техники в аэропорту, на железнодорожных или автовокзалах')
    msg = Var.bot.send_message(ms.chat.id, 'б)Оформлять витрины универмагов; заниматься оформлением шоурумов')

    if ms.text == 'а':
        Var.listDDO['ddo_x'] += 1
        Var.bot.register_next_step_handler(msg, answer_9)
    if ms.text == 'б':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_9)

def answer_9(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Выращивать и дрессировать служебных собак для поиска запрещенных веществ')
    with open('./images/images2Test/2_9a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Заниматься сборкой компьютеров или оборудования,налаживать их работу')
    with open('./images/images2Test/2_9b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_10)
    if ms.text == 'б':
        Var.listDDO['ddo_x'] += 1
        Var.bot.register_next_step_handler(msg, answer_10)

def answer_10(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Регулировать механизмы автомобиля, заменять или ремонтировать их в случае неисправности')
    with open('./images/images2Test/2_10a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Изучать жизнь организмов с помощью электронного микроскопа')
    with open('./images/images2Test/2_10b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_11)
    if ms.text == 'б':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_11)

def answer_11(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Работать с законами и кодексами, заверять документы, оформлять доверенности и договоры')
    with open('./images/images2Test/2_11a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Налаживать работу медицинского лазера, ультразвуковой аппаратуры')
    with open('./images/images2Test/2_11b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_12)
    if ms.text == 'б':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_12)

def answer_12(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Заниматься разведкой источников нефти, газа и других полезных ископаемых')
    msg = Var.bot.send_message(ms.chat.id, 'б)Разрабатывать новые модели электронной бытовой техники')

    if ms.text == 'а':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_13)
    if ms.text == 'б':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_13)

def answer_13(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Заниматься техническим обслуживанием оборудования, контролировать его правильную эксплуатацию')
    msg = Var.bot.send_message(ms.chat.id, 'б)Работать со статистическими данными страховой компании, на основе их анализа рассчитывать страховые тарифы')


    if ms.text == 'а':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_14)
    if ms.text == 'б':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_14)

def answer_14(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Преподавать какие-либо предметы в школе, техникуме, институте и т. д.')
    with open('./images/images2Test/2_14a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Работать в фондах архивов, находить необходимые документы')
    with open('./images/images2Test/2_14b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_15)
    if ms.text == 'б':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_15)

def answer_15(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Заниматься созданием новых моделей одежды,учитывая тенденции моды и индивидуальные особенности потребителя')
    with open('./images/images2Test/2_15a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Упорядочивать документацию фирмы и подготавливать новую (договора, счета,ведомости, доверенности и т. п.)')
    with open('./images/images2Test/2_15b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_ch'] += 1
        Var.bot.register_next_step_handler(msg, answer_16)
    if ms.text == 'б':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_16)

def answer_16(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Консультировать людей относительно туристических маршрутов других городов и стран')
    with open('./images/images2Test/2_16a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Разрабатывать сценарии праздников и торжественных событий, проводить их')
    with open('./images/images2Test/2_16b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_x'] += 1
        Var.bot.register_next_step_handler(msg, answer_17)
    if ms.text == 'б':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_17)

def answer_17(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Руководить комплексом работ по рациональному использованию, воспроизводству и защите леса в лесничестве')
    msg = Var.bot.send_message(ms.chat.id, 'б)Оформлять, иллюстрировать сайты, книги, журналы')

    if ms.text == 'а':
        Var.listDDO['ddo_ch'] += 1
        Var.bot.register_next_step_handler(msg, answer_18)
    if ms.text == 'б':
        Var.listDDO['ddo_x'] += 1
        Var.bot.register_next_step_handler(msg, answer_18)

def answer_18(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Играть на сцене, сниматься в кино, ставить трюки')
    with open('./images/images2Test/2_18a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Проводить клинические испытания новых лекарственных препаратов на живых объектах')
    with open('./images/images2Test/2_18b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_19)
    if ms.text == 'б':
        Var.listDDO['ddo_x'] += 1
        Var.bot.register_next_step_handler(msg, answer_19)

def answer_19(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Разрабатывать и писать сценарии для рекламного ролика, подбирать творческую команду артистов, музыкантов, гримеров и т. д.')
    msg = Var.bot.send_message(ms.chat.id, 'б)Следить за безопасностью компьютерной сети организации, обеспечивать её оптимальную работоспособность для пользователей')

    if ms.text == 'а':
        Var.listDDO['ddo_x'] += 1
        Var.bot.register_next_step_handler(msg, answer_20)
    if ms.text == 'б':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_20)
def answer_20(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Исправлять смысловые и стилистические ошибки в подготавливаемых для печати текстах')
    with open('./images/images2Test/2_20a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Оказывать людям психологическую помощь, работатьна телефоне доверия')
    with open('./images/images2Test/2_20b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_x'] += 1
        Var.bot.register_next_step_handler(msg, answer_21)
    if ms.text == 'б':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_21)

def answer_21(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Переводить научные тексты')
    msg = Var.bot.send_message(ms.chat.id, 'б)Производить архитектурно-восстановительные работы исторических мест')
    

    if ms.text == 'а':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_22)
    if ms.text == 'б':
        Var.listDDO['ddo_ch'] += 1
        Var.bot.register_next_step_handler(msg, answer_22)
def answer_22(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Изучать и анализировать ситуацию на фондовом рынке, покупать и перепродавать ценные бумаги, подводить итоги сделок')
    msg = Var.bot.send_message(ms.chat.id, 'б)Проводить геологические изыскания, участвоватьв экспедициях, посвященных изучению природных явлений')


    if ms.text == 'а':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_23)
    if ms.text == 'б':
        Var.listDDO['ddo_x'] += 1
        Var.bot.register_next_step_handler(msg, answer_23)
def answer_23(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Изучать генетику, выводить новые сорта растений')
    with open('./images/images2Test/2_23a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Контролировать и поддерживать правопорядок, предупреждать преступления, следить за безопасностью жизни и здоровья людей')
    with open('./images/images2Test/2_23b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_24)
    if ms.text == 'б':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_24)

def answer_24(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Сопровождать пассажиров во время воздушных или водных рейсов, консультировать их во время перелёта или плавания по технике безопасности')
    with open('./images/images2Test/2_24a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Проектировать новое производственное оборудование, дома')
    with open('./images/images2Test/2_24b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_25)
    if ms.text == 'б':
        Var.listDDO['ddo_ch'] += 1
        Var.bot.register_next_step_handler(msg, answer_25)

def answer_25(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Анализировать состояние растений и животных в загрязненных условиях среды')
    msg = Var.bot.send_message(ms.chat.id, 'б)Сопровождать людей в сложных туристических походах в роли инструктора')

    if ms.text == 'а':
        Var.listDDO['ddo_ch'] += 1
        Var.bot.register_next_step_handler(msg, answer_26)
    if ms.text == 'б':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, answer_26)
def answer_26(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Заниматься написанием востребованных текстов для интернет-сайтов, формировать поисковые запросы по ключевым словам и т. д.')
    msg = Var.bot.send_message(ms.chat.id, 'б)Производить химико-биологический анализ материалов, поступивших в лабораторию')


    if ms.text == 'а':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_27)
    if ms.text == 'б':
        Var.listDDO['ddo_ch'] += 1
        Var.bot.register_next_step_handler(msg, answer_27)

def answer_27(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Осуществлять взаимодействие с органами власти и общественными организациями, оказывать информационно-аналитическое сопровождение избирательной кампании')
    msg = Var.bot.send_message(ms.chat.id, 'б)Писать мультипликационные сюжеты, создавать мультипликационных персонажей и декорации')

    if ms.text == 'а':
        Var.listDDO['ddo_z'] += 1
        Var.bot.register_next_step_handler(msg, answer_28)
    if ms.text == 'б':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_28)

def answer_28(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Искать нужных работников, подбирать персонал для различных фирм')
    with open('./images/images2Test/2_28a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Разрабатывать мероприятия по охране редких растений')
    with open('./images/images2Test/2_28b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_ch'] += 1
        Var.bot.register_next_step_handler(msg, answer_29)
    if ms.text == 'б':
        Var.listDDO['ddo_x'] += 1
        Var.bot.register_next_step_handler(msg, answer_29)

def answer_29(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Заниматься монтажом электро- и гидротехнического оборудования в соответствии с проектом')
    msg = Var.bot.send_message(ms.chat.id, 'б)Рассказывать о товаре, убеждать людей приобретать его')

    if ms.text == 'а':
        Var.listDDO['ddo_ch'] += 1
        Var.bot.register_next_step_handler(msg, answer_30)
    if ms.text == 'б':
        Var.listDDO['ddo_p'] += 1
        Var.bot.register_next_step_handler(msg, answer_30)

def answer_30(ms):
    
    Var.bot.send_message(ms.chat.id, 'Выберите наиболее подходящий вам вариант(запишите букву варианта):')
    Var.bot.send_message(ms.chat.id, 'а)Проводить занятия с детьми по тренировке памяти, внимания, речи и т. д., организовывать игры, праздники, экскурсии и другие развлекательные мероприятия для детей')
    with open('./images/images2Test/2_30a.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    msg = Var.bot.send_message(ms.chat.id, 'б)Проектировать садово-парковые зоны, оформлять участки с помощью растений')
    with open('./images/images2Test/2_30b.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)

    if ms.text == 'а':
        Var.listDDO['ddo_t'] += 1
        Var.bot.register_next_step_handler(msg, show_preference)
    if ms.text == 'б':
        Var.listDDO['ddo_ch'] += 1
        Var.bot.register_next_step_handler(msg, show_preference)


def show_preference(ms):    # проверка макмимаального значения из словаря и вывод результата второго теста
    '''проверка на тест 2'''

    if ms.text == 'a':
        Var.listDDO['ddo_ch'] += 1
    else:
        Var.listDDO['ddo_x'] += 1

    max_key = max(Var.listDDO, key=Var.listDDO.get)

    if  max_key == 'ddo_p':
        Var.answersBasedOn3Tests.append('ddo_p')
        msg = Var.bot.send_message(ms.chat.id, 'Примеры профессий «человек-природа» Эколог Агроном Микробиолог Зоотехник Гидробиолог Агрохимик Фитопатолог Орнитолог Лесовод Полевод Цветовод Овощевод Птицевод Животновод Садовод Пчеловод Ветеринар.\nОсталось совсем чуть-чуть!Не хочешь ли ты пройти тест: «направление будущей профессии»?Это позволит узнать в какой области находится подходящая вам профессия',
            reply_markup=Var.markup_items_false_true)
        Var.bot.register_next_step_handler(msg, test_3_if_answer_true_1)
    if max_key == 'ddo_t' :
        Var.answersBasedOn3Tests.append('ddo_t')
        msg = Var.bot.send_message(ms.chat.id, 'В профессиях данного типа (примеры: слесарь-сборщик, техник-механик, инженер-механик, электрослесарь, инженер-электрик, техник-технолог\nОсталось совсем чуть-чуть!Не хочешь ли ты пройти тест: «направление будущей профессии»?Это позволит узнать в какой области находится подходящая вам профессия',
            reply_markup=Var.markup_items_false_true)
        Var.bot.register_next_step_handler(msg, test_3_if_answer_true_1)
    if max_key == 'ddo_ch':
        Var.answersBasedOn3Tests.append('ddo_ch')
        msg = Var.bot.send_message(ms.chat.id, 'Вот  профессии типа «человек-человек»: учитель, преподаватель,  психолог, социолог, социальный работник, педагог-психолог, дефектолог, логопед врач, медсестра, фельдшер, фармацевт, психолог-консультант\nОсталось совсем чуть-чуть!Не хочешь ли ты пройти тест: «направление будущей профессии»?Это позволит узнать в какой области находится подходящая вам профессия',
            reply_markup=Var.markup_items_false_true)
        Var.bot.register_next_step_handler(msg, test_3_if_answer_true_1)
    if max_key == 'ddo_z':
        Var.answersBasedOn3Tests.append('ddo_z')
        msg = Var.bot.send_message(ms.chat.id, 'Список профессий типа «человек-знаковая система». : программист; бухгалтер; лингвист, переводчик; редактор; инженер-конструктор; картограф; экономист, аналитик; системный администратор; архивист; логист\nОсталось совсем чуть-чуть!Не хочешь ли ты пройти тест: «направление будущей профессии»?Это позволит узнать в какой области находится подходящая вам профессия',
            reply_markup=Var.markup_items_false_true)
        Var.bot.register_next_step_handler(msg, test_3_if_answer_true_1)
    if max_key == 'ddo_x':
        Var.answersBasedOn3Tests.append('ddo_x')
        msg = Var.bot.send_message(ms.chat.id, 'К типу «человек-художественный образ» относятся профессии: художник, модельер, композитор, писатель, сценарист, режиссер, хореограф ,актер, музыкант-исполнитель, артист балета,  ювелир, парикмахер.\nОсталось совсем чуть-чуть!Не хочешь ли ты пройти тест: «направление будущей профессии»?Это позволит узнать в какой области находится подходящая вам профессия',
            reply_markup=Var.markup_items_false_true)
        Var.bot.register_next_step_handler(msg, test_3_if_answer_true_1)

def test_3_if_answer_true_1(ms):
    if ms.text == 'Да 🔥':
        markup_items = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
        item_a = types.InlineKeyboardButton(text='Аудиал')
        item_b = types.InlineKeyboardButton(text='Визуал')
        item_c = types.InlineKeyboardButton(text='Кинестетик')
        markup_items.add(item_a, item_b, item_c)

        msg = Var.bot.send_message(ms.chat.id, 'Кто ты по типу информации?',
            reply_markup=markup_items)
        Var.bot.register_next_step_handler(msg, test3.answer_2)
    else:
        if Var.ddo_p == 3:
            msg = Var.bot.send_message(ms.chat.id, 'Вам подходят профессии типа "человек-природа". Примеры профессий «человек-природа» Эколог Агроном Микробиолог Зоотехник Гидробиолог Агрохимик Фитопатолог Орнитолог Лесовод Полевод Цветовод Овощевод Птицевод Животновод Садовод Пчеловод Ветеринар')
        if Var.ddo_t == 3:
            msg = Var.bot.send_message(ms.chat.id, 'Вам подходят профессии типа "человек-техника". В профессиях данного типа (примеры: слесарь-сборщик, техник-механик, инженер-механик, электрослесарь, инженер-электрик, техник-техноло')
        if Var.ddo_ch == 3:
            msg = Var.bot.send_message(ms.chat.id, 'Вам подходят профессии типа "человек-человек". Вот  профессии типа «человек-человек»: учитель, преподаватель,  психолог, социолог, социальный работник, педагог-психолог, дефектолог, логопед врач, медсестра, фельдшер, фармацевт, психолог-консультан')
        if Var.ddo_z == 2:
            msg = Var.bot.send_message(ms.chat.id, 'Вам подходят профессии типа "человек-знаковая система". Список профессий типа «человек-знаковая система». : программист; бухгалтер; лингвист, переводчик; редактор; инженер-конструктор; картограф; экономист, аналитик; системный администратор; архивист; логис')
        if Var.ddo_x == 3:
            msg = Var.bot.send_message(ms.chat.id, 'Вам подходят профессии типа "человек-художественный образ". К типу «человек-художественный образ» относятся профессии: художник, модельер, композитор, писатель, сценарист, режиссер, хореограф ,актер, музыкант-исполнитель, артист балета,  ювелир, парикмахер')
   