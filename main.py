import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('5845828322:AAF45otX3O0_f_PHeQ8u9fLu_t8Nf263ygc')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    description = types.KeyboardButton('О НАСℹ️')
    stocks = types.KeyboardButton('АКЦИИ📈')
    price = types.KeyboardButton('ПРАЙС💵')
    doctors = types.KeyboardButton('ВРАЧИ-СПЕЦИАЛИСТЫ🧑‍⚕️')
    website = types.KeyboardButton('ВЕБ-САЙТ👩🏻‍💻')
    record = types.KeyboardButton('ЗАПИСАТЬСЯ👩🏻')
    sql = types.KeyboardButton('Когда я записан на приём?')
    markup.add(description, stocks, price, doctors, website, record, sql)
    bot.send_message(message.chat.id,
                     f'Добрый день, <b>{message.from_user.first_name}</b>! Вы обратились в Центр Диагностики Дзержинск 🏥',
                     parse_mode= 'html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def choice(message):
    if message.text == 'ВРАЧИ-СПЕЦИАЛИСТЫ🧑‍⚕️':
        doctors = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        neurosurgeon = types.KeyboardButton('НЕЙРОХИРУРГ')
        therapist = types.KeyboardButton('ТЕРАПЕВТ')
        cardiologist = types.KeyboardButton('КАРДИОЛОГ')
        neurologist = types.KeyboardButton('НЕВРОЛОГ')
        endocrinologist = types.KeyboardButton('ЭНДОКРИНОЛОГ')
        gynecologist = types.KeyboardButton('ГИНЕКОЛОГ')
        exit = types.KeyboardButton('ВЕРНУТЬСЯ НАЗАД🔙')
        doctors.add(neurosurgeon, therapist, cardiologist, neurologist, endocrinologist, gynecologist, exit)
        bot.send_message(message.chat.id, 'Какой врач Вас интересует?', reply_markup=doctors)

    elif message.text == "НЕЙРОХИРУРГ":
        doctor1 = open('1.jpg', 'rb')
        bot.send_photo(message.chat.id, doctor1)
        bot.send_message(message.chat.id, f'ФИО: <b>Яшин Константин Сергеевич</b>\n'
                                          f'ОПИСАНИЕ ДЕЯТЕЛЬНОСТИ ВРАЧА: Злокачественные и доброкачественные опухоли головного мозга,'
                                          f' лицевые боли, невралгия тройничного нерва, хирургическое лечение эпилепсии,'
                                          f' последствия черепно-мозговых травм, пластика дефектов костей свода и'
                                          f' основание черепа, гидроцефалия, функциональная'
                                          f' нейрохирургия.', parse_mode='html')

        doctor2 = open('2.jpeg', 'rb')
        bot.send_photo(message.chat.id, doctor2)
        bot.send_message(message.chat.id, f'ФИО: <b>Лазарь Андрей Даниилович</b>\n'
                                          f'ОПИСАНИЕ ДЕЯТЕЛЬНОСТИ ВРАЧА: Опухоли центральной нервной системы, '
                                          f' сосудистые заболевания нервной системы, черепно-мозговые травмы и их последствия, '
                                          f' травмы позвоночника и спинного мозга, дегенеративные поражения позвоночника, '
                                          f' эпилепсия, невралгия тройничного нерва, травмы периферических нервов.', parse_mode='html')

    elif message.text == "ТЕРАПЕВТ":
        doctor3 = open('3.jpg', 'rb')
        bot.send_photo(message.chat.id, doctor3)
        bot.send_message(message.chat.id, f'ФИО: <b>Шилова Александра Викторовна</b>\n'
                                          f'ОПИСАНИЕ ДЕЯТЕЛЬНОСТИ ВРАЧА: Проведение узи-исследований всех органов и систем человеческого организма, изучение состояния'
                                          f' сосудов головного мозга, шеи, верхних и нижних конечностей, исследование на предмет патологий сердце, '
                                          f'молочные железы, суставы, брюшную полость и забрюшное пространство, органы малого таза (и у женщин, и у мужчин), '
                                          f'лимфоузлы. Александра Викторовна имеет сертификат по специальности «Ультразвуковая диагностика», действие '
                                          f'которого регулярно подтверждает. Врачебной практикой занимается более 13 лет.', parse_mode='html')

    elif message.text == "КАРДИОЛОГ":
        doctor4 = open('4.jpg', 'rb')
        bot.send_photo(message.chat.id, doctor4)
        bot.send_message(message.chat.id, f'ФИО: <b>Смирнова Мария Владимировна</b>\n'
                                          f'ОПИСАНИЕ ДЕЯТЕЛЬНОСТИ ВРАЧА: В 2014 году окончила Нижегородскую Медицинскую академию.'
                                          f' После окончания обучения проработала врачом-терапевтом на базе приемного'
                                          f' покоя Городской Клинической больницы №13. В 2017 году получила'
                                          f' специализацию по кардиологии, вела пациентов кардиохирургического '
                                          f' отделения стационара. Диагностика любых видов боли в груди, контроль '
                                          f' и назначение адекватной терапии при гипертонической болезни, '
                                          f' выявление и коррекция всех видов аритмий, наблюдение и лечение пациентов с '
                                          f'ишемической болезнью сердца, ведение и реабилитация пациентов после восстановления '
                                          f'проходимости артерий сердца, лечение тромбозов и подбор антитромботической терапии.', parse_mode='html')
        doctor5 = open('5.jpg', 'rb')
        bot.send_photo(message.chat.id, doctor5)
        bot.send_message(message.chat.id, f'ФИО: <b>Волков Артем Александрович</b>\n'
                                          f'ОПИСАНИЕ ДЕЯТЕЛЬНОСТИ ВРАЧА: Занимается диагностикой, лечением заболеваний дыхательной системы, '
                                          f'заболевания суставов, проведением функции внешнего дыхания, электрокардионрамма, '
                                          f'проведение пульсоксиметрии. Диагностирует, лечит и предупреждает воспалительные, '
                                          f'метаболические и дегенеративно-дисторофические патологии сердца, сосудов. '
                                          f'Занимается реабилитацией пациентов, которые перенесли сердечно-сосудистые заболевания, '
                                          f'операции на сердце, сосудах.', parse_mode='html')

    elif message.text == "НЕВРОЛОГ":
        doctor6 = open('6.jpg', 'rb')
        bot.send_photo(message.chat.id, doctor6)
        bot.send_message(message.chat.id, f'ФИО: <b>Клюева Ирина Геннадьевна</b>\n'
                                          f'ОПИСАНИЕ ДЕЯТЕЛЬНОСТИ ВРАЧА: Закончила Нижегородскую государственную медицинскую академию в 1996 г.\n'
                                          f'Свидетельство о повышении квалификации №940/27 от 2011 г. по специальности «НЕВРОЛОГИЯ»,'
                                          f' выдано в ГБОУ ДПО «Российская медицинская академия последипломного образования» Минздравсоцразвития России;\n'
                                          f'Cертификат №0152240478895 от 6 марта 2015 г. по специальности «УЛЬТРАЗВУКОВАЯ ДИАГНОСТИКА»  ГБОУ ВПО НижГМА Минздрава России;\n'
                                          f'Удостоверение №522406530472 от 8 декабря 2017 г. о повышении квалификации по специальности «ЭКСТРАПИРАМИДАЛЬНЫЕ РАССТРОЙСТВА»'
                                          f' решением аттестационной комиссии Министерства здравоохранения РФ;\n'
                                          f'Удостоверение №523100570530 от 15.03.2019 г. о повышении квалификации по специальности «НЕВРОЛОГИЯ»,'
                                          f' выдано ФГБОУ ВО «ПИМУ» Минздрава России.', parse_mode='html')
    elif message.text == "ЭНДОКРИНОЛОГ":
        doctor7 = open('7.jpg', 'rb')
        bot.send_photo(message.chat.id, doctor7)
        bot.send_message(message.chat.id, f'ФИО: <b>Малышева Екатерина Сергеевна</b>\n'
                                          f'ОПИСАНИЕ ДЕЯТЕЛЬНОСТИ ВРАЧА: Гипотиреоз, диабет всех типов, зоб (диффузный, узловой, кистозный),'
                                          f' ожирение, остеопороз, тиреоидит, нарушение метаболизма кальция,'
                                          f' метаболический синдром. Кроме того,  специализируется на лечении диабета '
                                          f' помощью помповой инсулинотерапии.', parse_mode='html')
        doctor8 = open('8.jpg', 'rb')
        bot.send_photo(message.chat.id, doctor8)
        bot.send_message(message.chat.id, f'ФИО: <b>Селезнева Светлана Владимировна</b>\n'
                                          f'ОПИСАНИЕ ДЕЯТЕЛЬНОСТИ ВРАЧА: Закончила НМА в 1996 году, проходила интернатуру на базе'
                                          f' городской больницы №2 с 1996г по  1997 г. города Дзержинска;\n'
                                          f'Терапевт в поликлинике №1 с 1997 года по 2005 г;\n'
                                          f'В 2005 году  прошла первичную переподготовку по специальности  эндокринология;\n'
                                          f'В 2015 году получила  высшую квалификационную категорию по эндокринологии;\n'
                                          f'В 2007 году прошла первичную переподготовку по УЗД;\n'
                                          f'Прошла курсы повышения квалификации по УЗД сосудов в 2016 году, 2019 году и в 2021 году;\n'
                                          f'Каждые пять лет проходит курсы повышения квалификации, систематически посещает'
                                          f' тематические вебинары и конференции.', parse_mode='html')

    elif message.text == "ГИНЕКОЛОГ":
        doctor9 = open('9.png', 'rb')
        bot.send_photo(message.chat.id, doctor9)
        bot.send_message(message.chat.id, f'ФИО: <b>Дюдина Ксения Алексеевна</b>\n'
                                          f'ОПИСАНИЕ ДЕЯТЕЛЬНОСТИ ВРАЧА: 2008-2014 г. - НижГМА Лечебное дело 115224 №0222520;\n'
                                          f'Интернатура по специальности акушерство и гинекология;\n'
                                          f'2019 г. - переподготовка на врача УЗД;\n'
                                          f'2022 г. - повышение квалификации в «Академии постдипломного '
                                          f'образования ФНКЦ ФМБА России» в г.Москва;\n'
                                          f'В настоящее время работает в ГБУЗ НО «Дзержинский перинатальный центр».', parse_mode='html')

    elif message.text == 'ВЕРНУТЬСЯ НАЗАД🔙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        description = types.KeyboardButton('О НАСℹ️')
        stocks = types.KeyboardButton('АКЦИИ📈')
        price = types.KeyboardButton('ПРАЙС💵')
        doctors = types.KeyboardButton('ВРАЧИ-СПЕЦИАЛИСТЫ🧑‍⚕️')
        website = types.KeyboardButton('ВЕБ-САЙТ👩🏻‍💻')
        record = types.KeyboardButton('ЗАПИСАТЬСЯ👩🏻')
        markup.add(description, stocks, price, doctors, website, record)
        bot.send_message(message.chat.id, 'Вы вернулись в основное меню!', reply_markup=markup)

    elif message.text == 'О НАСℹ️':
        bot.send_message(message.chat.id, 'ООО «Центр Диагностики Дзержинск» - это многопрофильная клиника, оказывающая весь спектр услуг, таких как прием врачей - специалистов, МРТ, УЗИ, анализы.\n'
                                          '📞 +7 (930)-283-84-27\n'
                                          '📍 г. Дзержинск, ул. Буденного, дом 2Б\n'
                                          '✉️ cd-mrt@bk.ru')
    elif message.text == 'АКЦИИ📈':
        bot.send_message(message.chat.id,
                         '<b>АКЦИЯ №1:</b> Консультация кардиолога + ЭхоКГ + ЭКГ - 2500 руб;\n'
                         '<b>АКЦИЯ №2:</b> 30% скидка на все виды анализов;\n'
                         '<b>АКЦИЯ №3:</b> УЗИ сосудов головного мозга и шеи - 1800 руб;\n'
                         '<b>АКЦИЯ №4:</b> УЗИ вен и артерий нижних конечностей - 1800 руб;\n'
                         '<b>АКЦИЯ №5:</b> 10% скидка на анализы после консультации наших врачей;\n'
                         '<b>АКЦИЯ №6:</b> 20% скидка на приём к гастроэнтерологу после УЗИ/МРТ брюшной полости.', parse_mode='html')

    elif message.text == 'ПРАЙС💵':
        bot.send_message(message.chat.id, 'Файл с ценами на предоставляемые услуги!')
        price = open('price.doc', 'rb')
        bot.send_document(message.chat.id, price)

    elif message.text == 'ВЕБ-САЙТ👩🏻‍💻':
        markup = types.InlineKeyboardMarkup()
        website = types.InlineKeyboardButton("ВЕБ-САЙТ👩🏻‍💻", url='https://clck.ru/32sQ3k')
        markup.add(website)
        bot.send_message(message.chat.id, 'Официальный сайт, где собрана вся информация о нашем медицинском центре👇🏻', reply_markup=markup)

    elif message.text == 'ЗАПИСАТЬСЯ👩🏻':
        markup = types.InlineKeyboardMarkup()
        website = types.InlineKeyboardButton("ВЕБ-САЙТ👩🏻‍💻", url='http://127.0.0.1:5000/')
        markup.add(website)
        bot.send_message(message.chat.id, 'Официальный сайт, где можно записаться на прием к врачу👇🏻', reply_markup=markup)


    else:
        return

bot.polling(none_stop=True)
