import Variabelsbot as Var
from telebot import types


def answer_2(ms):   # фукнция отвечает за 2 задание третьего теста
    markup_items = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    item_a = types.InlineKeyboardButton(text='Отправлюсь в путешествие')
    item_b = types.InlineKeyboardButton(text='Встречусь с творческой личностью')
    item_c = types.InlineKeyboardButton(text='Засяду за журналом с научными фактами')
    markup_items.add(item_a, item_b, item_c)

    msg = Var.bot.send_message(ms.chat.id, '2. У тебя есть три варианта,как ты проведещь выходные,какой из них ты выберешь?',
        reply_markup=markup_items)
    with open('./images/3_1.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    
    if ms.text == 'Аудиал':
        Var.direction['direction_a'] += 1
        Var.bot.register_next_step_handler(msg, answer_3)
    if ms.text == 'Визуал':
        Var.direction['direction_b'] += 1
        Var.bot.register_next_step_handler(msg, answer_3)
    if ms.text == 'Кинестетик':
        Var.direction['direction_c'] += 1
        Var.bot.register_next_step_handler(msg, answer_3)
    

def answer_3(ms):   # фукнция отвечает за 3 задание третьего теста
    
    markup_items = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    item_a = types.InlineKeyboardButton(text='математика,физика,информатика')
    item_b = types.InlineKeyboardButton(text='химия,биология,география')
    item_c = types.InlineKeyboardButton(text='обществознание,литература,история')

    markup_items.add(item_a, item_b, item_c)

    msg = Var.bot.send_message(ms.chat.id, '3. Какие предметы давались вам лучше всего?',
        reply_markup=markup_items)

    if ms.text == 'Отправлюсь в путешествие':
        Var.direction['direction_a'] += 1
        Var.bot.register_next_step_handler(msg, answer_4)
    if ms.text == 'Встречусь с творческой личностью':
        Var.direction['direction_b'] += 1
        Var.bot.register_next_step_handler(msg, answer_4)
    if ms.text == 'Засяду за журналом с научными фактами':
        Var.direction['direction_c'] += 1
        Var.bot.register_next_step_handler(msg, answer_4)

def answer_4(ms):
    
    markup_items = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=1)
    item_a = types.InlineKeyboardButton(text='Творить или общаться с кем-то')
    item_b = types.InlineKeyboardButton(text='Работать с числами,или работать с техникой')
    item_c = types.InlineKeyboardButton(text='Ухаживать за растениями / животными')

    markup_items.add(item_a, item_b, item_c)

    msg = Var.bot.send_message(ms.chat.id, '4. Ваши друзья замечают и говорят, что у вас хорошо получается...?',
        reply_markup=markup_items)
    with open('./images/4_1.png', "rb") as file:
        Var.bot.send_photo(ms.chat.id, file)
    
    if ms.text == 'математика,физика,информатика':
        Var.direction['direction_a'] += 1
        Var.bot.register_next_step_handler(msg, result)
    if ms.text == 'химия,биология,география':
        Var.direction['direction_b'] += 1
        Var.bot.register_next_step_handler(msg, result)
    if ms.text == 'обществознание,литература,история':
        Var.direction['direction_c'] += 1
        Var.bot.register_next_step_handler(msg, result)

def result(ms):    
    
    if ms.text == 'Творить или общаться с кем-то':
        Var.direction['direction_a'] += 1
    if ms.text == 'Работать с числами,или работать с техникой':
        Var.direction['direction_b'] += 1
    if ms.text == 'Ухаживать за растениями / животными':
        Var.direction['direction_c'] += 1

    max_key = max(Var.direction, key=Var.direction.get)
    Var.answersBasedOn3Tests.append(f'{max_key}')

    if max_key == 'direction_a':
        Var.bot.send_message(ms.chat.id, 'социальное направление')
    if max_key == 'direction_b':
        Var.bot.send_message(ms.chat.id, 'физматическое направление')
    if max_key == 'direction_c':
        Var.bot.send_message(ms.chat.id, 'химико-биологическое направление')

    msg = Var.bot.send_message(ms.chat.id, 'Перейдем к результату на основе 3 тестов?', reply_markup=Var.markup_items_false_true)
    Var.bot.register_next_step_handler(msg, result_all)

def result_all(ms):     # выведение результатов на основе трех тестов 
    if ms.text == 'Да 🔥':
        if Var.answersBasedOn3Tests[0] == 'Флегматик':
            if Var.answersBasedOn3Tests[1] == 'ddo_p':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧП(человек-природа)-социо,и вам подходят такие профессии: Архитектор,ландшафтный дизайнер,врач,психолог,Психолог ,Учитель')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧП(человек-природа)-физмат,и вам подходят такие профессии: Учёный исследователь,специалист по обработке данных,специалист по сбору данных')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧП(человек-природа)-химбио,и вам подходят такие профессии: Биотехнолог. Эколог  Агропромышленный инженер . Ветеринар . Специалист по охране окружающей среды . Фармацевт')
            if Var.answersBasedOn3Tests[1] == 'ddo_t':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧТ(человек-техника)-социо,и вам подходят такие профессии: Руководитель проекта.Специалист по продажам технического оборудования . IT-консультант. Инженер по системам управления')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧТ(человек-техника)-физмат,и вам подходят такие профессии: Инженер по автоматизации  Аналитик данных  Специалист по информационным технологиям ')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик-ЧТ(человек-техника)-химбио,и вам подходят такие профессии: Химик-технолог . Специалист по экологии и охране окружающей среды . Научный сотрудник в области химии или биологии')
            if Var.answersBasedOn3Tests[1] == 'ddo_ch':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧЧ(человек-человек)-социо,и вам подходят такие профессии: Юрист,менеджер,адвокат,учитель')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧЧ(человек-человек)-физмат,и вам подходят такие профессии: Специалист по образовательным программам в STEM Координатор научных исследований')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧЧ(человек-человек)-химбио,и вам подходят такие профессии: Хирург,анестезиолог,терапевт,психолог')
            if Var.answersBasedOn3Tests[1] == 'ddo_z':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧЗС(человек-знаковая система)-социо,и вам подходят такие профессии: Журналист . Социальный работник  Маркетолог.Специалист по связям с общественностью')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧЧ(человек-человек)-физмат,и вам подходят такие профессии: Специалист по образовательным программам в STEM Координатор научных исследований')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧЗС(человек-знаковая система)-химбио,и вам подходят такие профессии: Ученый исследователь,специалист по обработке данных,Биотехнолог  Инженер-химик')
            if Var.answersBasedOn3Tests[1] == 'ddo_x':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧХО(человек-художественный образ)-социо,и вам подходят такие профессии: Актер,продюссер,режисер,артист балета и театра')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧХО(человек-художественный образ)-физмат,и вам подходят такие профессии: Разработчик образовательных игр с научным содержанием . Архитектор с акцентом на инновационные технологии')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Холерик- ЧХО(человек-художественный образ)-химбио,и вам подходят такие профессии: Мастер маникюра,ресниц,бровей,визажист,парикмахер')
        if Var.answersBasedOn3Tests[0] == 'Меланхолик':
            if Var.answersBasedOn3Tests[1] == 'ddo_p':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик-ЧП(человек-природа)-социо,и вам подходят такие профессии: учитель естественных наук,работник природохранительных организаций,экологический консультант')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик-ЧП(человек-природа)-физмат,и вам подходят такие профессии: экскурсовод, работник с данными в сфере биологических данных')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик-ЧП,и вам подходят такие профессии:-химбио,и вам подходят такие профессии: эколог , зоолог, ветеринар, биолог')
            if Var.answersBasedOn3Tests[1] == 'ddo_t':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧТ(человек-техника)-социо,и вам подходят такие профессии: IT-консультант. Инженер по системам управления,учитель информатики,бухгалтер')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧТ(человек-техника)-физмат,и вам подходят такие профессии: Программист  Инженер-математик . Разработчик программного обеспечения')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик-ЧТ(человек-техника)-химбио,и вам подходят такие профессии: Биотехнолог, Инженер-химик,Микробиолог')
            if Var.answersBasedOn3Tests[1] == 'ddo_ch':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧЧ(человек-человек)-социо,и вам подходят такие профессии: риелтор,менеджер,работник правоохранительных органов')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧЧ(человек-человек)-физмат,и вам подходят такие профессии: Научный консультант . Преподаватель физики или математики . Менеджер проектов в области науки и технологий')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧЧ(человек-человек)-химбио,и вам подходят такие профессии: медицинский работник,психолог,специалист по экологии')
            if Var.answersBasedOn3Tests[1] == 'ddo_z':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧЗС(человек-знаковая система)-социо,и вам подходят такие профессии: Социальный работник .. Маркетолог . Специалист по связям с общественностью')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧЗС(человек-знаковая система)-физмат,и вам подходят такие профессии: Инженер . Программист.Аналитик данных')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧЗС(человек-знаковая система)-химбио,и вам подходят такие профессии: Научный писатель (в химко-биологической сфере). Научный исследователь Редактор научных журналов. Специалист по биомедицинской информатике')
            if Var.answersBasedOn3Tests[1] == 'ddo_x':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧХО(человек-художественный образ)-социо,и вам подходят такие профессии:Работник балетной или театральной трупы,хореограф,педагог')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧХО(человек-художественный образ)-физмат,и вам подходят такие профессии:Научный иллюстратор . Дизайнер научной визуализации . Художник анимации в области образования ')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Меланхолик- ЧХО(человек-художественный образ)-химбио,и вам подходят такие профессии: визажист,мастер маникюра,домашний производитель(человек который дома готовит на заказ торты,свечи,мыло )')
        if Var.answersBasedOn3Tests[0] == 'Сангвиник':
            if Var.answersBasedOn3Tests[1] == 'ddo_p':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧП(человек-природа)-социо,и вам подходят такие профессии: Организатор мероприятий,Маркетолог,Менеджер по продажам')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧП(человек-природа)-физмат,и вам подходят такие профессии: Садовод ,ландшафтный дизайнер,Эколог')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧП(человек-природа)-химбио,и вам подходят такие профессии: Химик-органик,Фармаколог,Сельскохозяйственный инженер')
            if Var.answersBasedOn3Tests[1] == 'ddo_t':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧТ(человек-техника)-социо,и вам подходят такие профессии: Менеджер по продажам технического оборудования,Специалист по внедрению IT-решений,Инженер по маркетингу в области технологий')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧТ(человек-техника)-физмат,и вам подходят такие профессии: Инженер-исследователь,Системный аналитик,Финансовый аналитик')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧТ(человек-техника)-химбио,и вам подходят такие профессии: Инженер-химик,Медицинский лаборант,Биотехнолог')
            if Var.answersBasedOn3Tests[1] == 'ddo_ch':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧЧ(человек-человек)-социо,и вам подходят такие профессии: Психолог,Учитель, воспитатель,Менеджер по продажам')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧЧ(человек-человек)-физмат,и вам подходят такие профессии: Инженер по продажам,Менеджер проектов в IT,Научный консультант')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧЧ(человек-человек)-химбио,и вам подходят такие профессии: Медицинский работник,Специалист по продажам в области фармацевтики,Педагог в области естественных наук')
            if Var.answersBasedOn3Tests[1] == 'ddo_z':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧЗС(человек-знаковая система)-социо,и вам подходят такие профессии: Специалист по связям с общественностью,Психолог,Социолог')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧЗС(человек-знаковая система)-физмат,и вам подходят такие профессии: Разработчик программного обеспечения,IT-специалист,Инженер')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧЗС(человек-знаковая система)-химбио,и вам подходят такие профессии: Химический аналитик,Биологический исследователь,Специалист по клиническим испытаниям')
            if Var.answersBasedOn3Tests[1] == 'ddo_x':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧХО(человек-художественный образ)-социо,и вам подходят такие профессии: Журналист,сценарист,режисёр,преподаватель музыки')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник- ЧХО(человек-художественный образ)-физмат,и вам подходят такие профессии: Дизайнер научной визуализации . Художник анимации в области образования ')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-Сангвиник-ЧХО(человек-художественный образ)-химбио,и вам подходят такие профессии: Мастер маникюра,ресниц,бровей,визажист,парикмахер')
        if Var.answersBasedOn3Tests[0] == 'Холерик':
            if Var.answersBasedOn3Tests[1] == 'ddo_p':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧП(человек-природа)-социо,и вам подходят такие профессии: работник природохранительных организаций,экологический консультант')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧП(человек-природа)-физмат,и вам подходят такие профессии: Садовод ,ландшафтный дизайнер,Эколог')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧП(человек-природа)-химбио,и вам подходят такие профессии: Деревовод (лесное хозяйство). Агент по охране окружающей среды Биолог-эколог . Садовод или ландшафтный дизайнер . Гидробиолог  Специалист по экологии')
            if Var.answersBasedOn3Tests[1] == 'ddo_t':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧТ(человек-техника)-социо,и вам подходят такие профессии: Инженер по маркетингу в области технологий,Обучающий специалист по технологиям,Технический консультант')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧТ(человек-техника)-физмат,и вам подходят такие профессии: Финансовый аналитик,Программист-аналитик,Менеджер по проектам в области технологий')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧТ(человек-техника)-химбио,и вам подходят такие профессии: Химик-технолог . Специалист по экологии и охране окружающей среды . Научный сотрудник в области химии или биологии')
            if Var.answersBasedOn3Tests[1] == 'ddo_ch':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧЧ(человек-человек)-социо,и вам подходят такие профессии: Психолог,Учитель, воспитатель,Менеджер по продажам,консультант')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧЧ(человек-человек)-физмат,и вам подходят такие профессии: Специалист по образовательным программам в STEM Координатор научных исследований')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧЧ(человек-человек)-химбио,и вам подходят такие профессии: медицинский работник,психолог,специалист по экологии')
            if Var.answersBasedOn3Tests[1] == 'ddo_z':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧЗС(человек-знаковая система)-социо,и вам подходят такие профессии: Журналист . Социальный работник  Маркетолог.Специалист по связям с общественностью ')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧЗС(человек-знаковая система)-физмат,и вам подходят такие профессии: Инженер . Программист.Аналитик данных')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧЗС(человек-знаковая система)-химбио,и вам подходят такие профессии: Биологический исследователь,Специалист по клиническим испытаниям')
            if Var.answersBasedOn3Tests[1] == 'ddo_x':
                if Var.answersBasedOn3Tests[2] == 'direction_a':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧХО(человек-художественный образ)-социо,и вам подходят такие профессии:Журналист,сценарист,режисёр')
                if Var.answersBasedOn3Tests[2] == 'direction_b':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧХО(человек-художественный образ)-физмат,и вам подходят такие профессии: Разработчик образовательных игр с научным содержанием . Архитектор с акцентом на инновационные технологии')
                if Var.answersBasedOn3Tests[2] == 'direction_c':
                    Var.bot.send_message(ms.chat.id, 'Вы-флегматик-ЧХО(человек-художественный образ)-химбио,и вам подходят такие профессии: Мастер маникюра,ресниц,бровей,визажист,парикмахер')
    else:
        msg = Var.bot.send_message(ms.chat.id, 'Спасибо за прохождение теста , удачи вам в выборе профессии 🍀')