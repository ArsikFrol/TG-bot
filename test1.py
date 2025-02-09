import Variabelsbot as Var
from telebot import types

import test2

def answer_2(message):   # функция которая отвечает за 2 вопрос в первом тесте
    msg = Var.bot.send_message(message.chat.id, 'Легко ли вам обратиться на улице к незнакомому человеку?',
        reply_markup=Var.markup_items_false_true)
    Var.bot.register_next_step_handler(msg, answer_3)

def answer_3(message):   # функция которая отвечает за 3 вопрос в первом тесте
    msg = Var.bot.send_message(message.chat.id, 'Нравиться  ли вам работа, требующая быстрой реакции?',
        reply_markup=Var.markup_items_false_true)
    Var.bot.register_next_step_handler(msg, answer_4)

def answer_4(message):   # функция которая отвечает за 4 вопрос в первом тесте
    msg = Var.bot.send_message(message.chat.id, 'Любите ли рассказывать анекдоты?',
        reply_markup=Var.markup_items_false_true)
    Var.bot.register_next_step_handler(msg, answer_5)

def answer_5(message):
    msg = Var.bot.send_message(message.chat.id, 'Доводилось ли вам разыгрывать своих знакомых?',
        reply_markup=Var.markup_items_false_true)
    Var.bot.register_next_step_handler(msg, interim_1_results_1)

def interim_1_results_1(message):
    msg = Var.bot.send_message(message.chat.id, 'Подсчитайте свои ответы «Да» и запишите промежуточный результат:\nОт 0 до 2- ваш тип «M»\nОт 3 до 5- ваш тип «N»\nТеперь ответьте  ещё на 5 вопросов:\nБывают ли у вас резкие и внезапные перепады настроения?',
        reply_markup=Var.markup_items_false_true)
    Var.bot.register_next_step_handler(msg, answer_6)

def answer_6(message):
    msg = Var.bot.send_message(message.chat.id, 'Часто ли вам приходиться жалеть из-за того, что вы что-то сказали или сделали не подумав?',
        reply_markup=Var.markup_items_false_true)
    Var.bot.register_next_step_handler(msg, answer_7)
    
def answer_7(message):
    msg = Var.bot.send_message(message.chat.id, 'Легко ли вас обидеть?',
        reply_markup=Var.markup_items_false_true)
    Var.bot.register_next_step_handler(msg, answer_8)
    
def answer_8(message):
    msg = Var.bot.send_message(message.chat.id, 'Беспокоитесь ли вы о своём здоровье?',
        reply_markup=Var.markup_items_false_true)
    Var.bot.register_next_step_handler(msg, answer_9)
    
def answer_9(message):
    msg = Var.bot.send_message(message.chat.id, 'Волнует ли вас мнение окружающих?',
        reply_markup=Var.markup_items_false_true)
    Var.bot.register_next_step_handler(msg, interim_1_results_2)


def interim_1_results_2(message):
    msg = Var.bot.send_message(message.chat.id, 'Подсчитайте свои ответы «Да» и запишите промежуточный результат:\nОт 0 до 2 – ваш тип  «O»\nОт 3 до 5 – ваш тип «P»\nТеперь сложите результаты вместе, и вы узнаете свой темперамент:\n«MO» - вы флегматик\n«MP» - вы меланхолик\n«NO» - вы сангвиник\n«NP» - вы холерик.\nКакой темперменты вам ближе?', reply_markup=Var.markup_items_temp)
    Var.bot.register_next_step_handler(msg, show_temperament)

def show_temperament(ms):    # проверка результатов 1 теста
    if ms.text == 'Флегматик':
        Var.answersBasedOn3Tests.append('Флегматик')
        with open("./images/fleg.png", "rb") as photo:
            Var.bot.send_photo(ms.chat.id, photo)
        msg = Var.bot.send_message(ms.chat.id, 'Рекомендуемые профессии: машинопись , бухгалтерия, экономика, механик, электрик, инженер, агроном, водитель, научные – ботаник, астроном, физик, математик.\nТы молодец!А давай пройдём ещё один тест: «предрасположенность будущей профессии»?Он поможет определиться в какой сфере находиться подходящая вам профессия.',
            reply_markup=Var.markup_items_false_true)
        Var.bot.register_next_step_handler(msg, test_2_if_answer_true_1)
    if ms.text == 'Меланхолик':
        Var.answersBasedOn3Tests.append('Меланхолик')
        with open("./images/mel.png", "rb") as photo:
            Var.bot.send_photo(ms.chat.id, photo)
        msg = Var.bot.send_message(ms.chat.id, 'Рекомендуемые профессии: педагоги , деятели искусства, художник, швея-модельер, маляр, копировщик рисунков, композитор, писатель, ветеринарный врач, геолог, агроном, зоотехник, бухгалтер, машинопись, авто-слесарь, слесарь, токарь, радиомеханик и др. Склонность к творчеству, практическому труду, наблюдательности.\nТы молодец!А давай пройдём ещё один тест: «предрасположенность будущей профессии»?Он поможет определиться в какой сфере находиться подходящая вам профессия.',
            reply_markup=Var.markup_items_false_true)
        Var.bot.register_next_step_handler(msg, test_2_if_answer_true_1)
    if ms.text == 'Сангвиник':
        Var.answersBasedOn3Tests.append('Сангвиник')
        with open("./images/sang.png", "rb") as photo:
            Var.bot.send_photo(ms.chat.id, photo)
        msg = Var.bot.send_message(ms.chat.id, 'Рекомендуемые профессии: менеджер , учитель, врач, м/с общего профиля, психолог, воспитатель, организатор, продавец, официант, инженер-технолог и др. Обладает социальными умениями и нуждается в социальных контактах. Организаторские способности.\nТы молодец!А давай пройдём ещё один тест: «предрасположенность будущей профессии»?Он поможет определиться в какой сфере находиться подходящая вам профессия.',
            reply_markup=Var.markup_items_false_true)
        Var.bot.register_next_step_handler(msg, test_2_if_answer_true_1)
    if ms.text == 'Холерик':
        Var.answersBasedOn3Tests.append('Холерик')
        with open("./images/hol.png", "rb") as photo:
            Var.bot.send_photo(ms.chat.id, photo)
        msg = Var.bot.send_message(ms.chat.id, 'Рекомендуемые профессии: телерепортер , товаровед, артист, дипломат, журналист, снабженец, предприниматель и др. Обладает вербальными способностями. Избирает  задачи, позволяющие ему проявить свою  энергию, энтузиазм, импульсивность, доминантность, любовь к приключениям.\nТы молодец!А давай пройдём ещё один тест: «предрасположенность будущей профессии»?Он поможет определиться в какой сфере находиться подходящая вам профессия.',
            reply_markup=Var.markup_items_false_true)
        Var.bot.register_next_step_handler(msg, test_2_if_answer_true_1)


def test_2_if_answer_true_1(ms):   # функкция отвечающая за переход на второй тест

    if ms.text == 'Да 🔥':
        Var.bot.send_message(ms.chat.id, 'Второй тест ( А. Климова,А. Азбель) \nВыберите наиболее подходящий вам вариант(запишите букву варианта):\nа)Создавать, писать компьютерные программы, алгоритмы')
        with open('./images/images2Test/2_1a.png', "rb") as file:
            Var.bot.send_photo(ms.chat.id, file)
        msg = Var.bot.send_message(ms.chat.id, 'б)Консультировать людей в фитнес-зале, в бассейне, на спортивной площадке')
        with open('./images/images2Test/2_1b.png', "rb") as file:
            Var.bot.send_photo(ms.chat.id, file)

        Var.bot.register_next_step_handler(msg, test2.answer_2)
    else:
        if Var.answersBasedOn3Tests[0] == 'Флегматик':
            with open("./images/fleg.png", "rb") as photo:
                Var.bot.send_photo(ms.chat.id, photo)
            msg = Var.bot.send_message(ms.chat.id, 'Вы -флегматик.Флегматик — спокойный и ровный, невозмутимый, редко выходит из себя, к бурному выражению эмоций не склонен.  В зависимости от условий у такого человека могут сформироваться как положительные (выдержка, вдумчивость, глубина мыслей), так и отрицательные (пассивность, вялость, безразличие к окружающему) черты.Рекомендуемые профессии: машинопись , бухгалтерия, экономика, механик, электрик, инженер, агроном, водитель, научные – ботаник, астроном, физик, математик.')
        elif Var.answersBasedOn3Tests[0] == 'Меланхолик':
            with open("./images/mel.png", "rb") as photo:
                Var.bot.send_photo(ms.chat.id, photo)
            msg = Var.bot.send_message(ms.chat.id, 'Вы-меланхолик.Меланхолик — чувствительный, утонченный. Такой человек тонко реагирует на слабые раздражители, но сильные способны надолго вывести его из душевного равновесия. Однако внешне его переживания проявляются сдержанно. В благоприятных условиях это человек глубокий, содержательный, в неблагоприятных же может стать замкнутым, боязливым, тревожным. Рекомендуемые профессии: педагоги , деятели искусства, художник, швея-модельер, маляр, копировщик рисунков, композитор, писатель, ветеринарный врач, геолог, агроном, зоотехник, бухгалтер, машинопись, авто-слесарь, слесарь, токарь, радиомеханик и др. ')
        elif Var.answersBasedOn3Tests[0] == 'Сангвиник':
            with open("./images/sang.png", "rb") as photo:
                Var.bot.send_photo(ms.chat.id, photo)
            msg = Var.bot.send_message(ms.chat.id, 'Вы-сангвиник.Сангвиник — быстро приспосабливается к новым условиям, легко сходится с людьми, общителен. Сравнительно легко переживает неприятности, удары судьбы. При отсутствии серьезных целей может стать поверхностным, непостоянным.Рекомендуемые профессии: менеджер , учитель, врач, м/с общего профиля, психолог, воспитатель, организатор, продавец, официант, инженер-технолог и др')
        elif Var.answersBasedOn3Tests[0] == 'Холерик':
            with open("./images/hol.png", "rb") as photo:
                Var.bot.send_photo(ms.chat.id, photo)
            msg = Var.bot.send_message(ms.chat.id, 'Вы-холерик.Холерик — эмоционален, склонен к порывистым действиям, энергичен, активен и инициативен. Способен страстно отдаваться делу, которое его заинтересовало. Любит разнообразие во всем, нуждается в постоянных источниках новых ярких впечатлений. Плохо переносит однообразие, скуку — в таких условиях становится раздражительным, непоследовательным.Рекомендуемые профессии: телерепортер , товаровед, артист, дипломат, журналист, снабженец, предприниматель и др')


