import random
from telebot import TeleBot, types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import TOKEN
from info import *
from keyboard import *
from db import db

bot : TeleBot = TeleBot(TOKEN)#TOKEN)

from denis import *

######################################################MainFunctions#########################################################


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    bot.send_message(
        chat_id,
        f"""Привет {user_name}! 🖐

Я тебя не знаю 🤔

Давай познакомимся! Для этого тебе необходимо зарегистрироваться, нажав кнопку Создать семью.

Это позволит нам лучше узнать друга и дать тебе доступ ко всем функциям бота, такие как:
- Получать список досугов
- Редактировать профиль
И многое другое 🤯
Ты готов?
Если да, скорее нажимай кнопку «Создать семью» и делись информацией.
Это поможет нам лучше познакомиться! 👇""", reply_markup=main_menu)


@bot.message_handler(commands=['instruction'])
def send_instruction(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, """Инструкция бота 🧑‍💻📱
📃Использование команд:
▎Введите команду <u>/start</u>, чтобы увидеть меню.
▎Введите команду <u>/menu</u>, что-бы показать меню.

🆗Получение списка досуга:
▎Введите команду <u>/start</u>.
▎Нажмите на кнопку.
▎Выберите ваше местоположение.

👨‍👧‍👧Добавление пользователя:
▎Введите <u>/menu</u>.
▎Перейдите во вкладку семья.
▎Нажмите на кнопку редактировать.
▎Перейдите во вкладку добавить пользователя.
▎Введите его данные и нажмите далее.""", parse_mode="html", reply_markup=main_menu)

############################################################################################################################

@bot.callback_query_handler(func=lambda c:c.data == "instruction")
def send_instruction_callback(call: CallbackQuery):
    bot.edit_message_text("""Инструкция бота 🧑‍💻📱
📃Использование команд:
▎Введите команду <u>/start</u>, чтобы увидеть меню.
▎Введите команду <u>/menu</u>, что-бы показать меню.

🆗Получение списка досуга:
▎Введите команду <u>/start</u>.
▎Нажмите на кнопку.
▎Выберите ваше местоположение.

👨‍👧‍👧Добавление пользователя:
▎Введите <u>/menu</u>.
▎Перейдите во вкладку семья.
▎Нажмите на кнопку редактировать.
▎Перейдите во вкладку добавить пользователя.
▎Введите его данные и нажмите далее.""", call.message.chat.id, call.message.id, parse_mode="html", reply_markup=main_menu)

######################################################MenuFunctions#########################################################

@bot.message_handler(commands=['menu'])
def menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Перевожу в меню...", reply_markup=main_menu)

@bot.callback_query_handler(func=lambda c: c.data == ("menu"))
def menu_callback(call: CallbackQuery):
    bot.edit_message_text("Перевожу в меню...", call.message.chat.id, call.message.id, reply_markup=main_menu)


######################################################1#########################################################

@bot.callback_query_handler(func=lambda c: c.data == ("main_leisure"))
def main_leisure_menu(call: CallbackQuery):
    bot.edit_message_text("Где вам будет удобнее спланировать досуг?", call.message.chat.id, call.message.id, reply_markup=main_leisure)


######################################################AT_HOME#########################################################

@bot.callback_query_handler(func=lambda c: c.data == ("at_home"))
def at_home_step(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_r = choose_random_activity(activities)
    bot.edit_message_text(message_r, call.message.chat.id, call.message.id, parse_mode='Markdown', reply_markup=markup_get_activity)


@bot.callback_query_handler(func=lambda c: c.data == ("one_more_activity"))
def one_more_activity(call: CallbackQuery):
    bot.register_next_step_handler(call.message, at_home_step)


######################################################NOT_AT_HOME#########################################################

@bot.callback_query_handler(func=lambda c: c.data == ("not_at_home"))
def not_at_home_step(call: CallbackQuery):
#    chat_id = call.message.chat.id
#    list_of_interests = db.get_true_values_for_user(chat_id)
#    if len(list_of_interests) == 0:
#        bot.send_message(chat_id, """Oops! 😱 Вы отсутствуете в нашей базе данных.\n
#Не переживайте, просто заполните небольшую анкету, и мы вас зарегистрируем! 🎉""")
    markup = InlineKeyboardMarkup()
    markup.add(
        *[InlineKeyboardButton(i, callback_data=f"not_at_home>{escape(i)}") for i in location_data.keys()]
    )
    bot.edit_message_text("Где-бы вам было бы интересно провести время? 🤔", call.message.chat.id, call.message.id, reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data.startswith("not_at_home>"))
def not_at_home_choose(call: CallbackQuery):
    bot.delete_message(call.message.chat.id, call.message.id)

    category_name = unescape(call.data.split(">")[1])
    category = random.choice(list(location_data[category_name].values()))
    messages :list[int] = []
    for m in category.values():
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Подробнее", url=m[2]), row_width=1)
        messages.append(bot.send_photo(call.message.chat.id, m[0], m[1], parse_mode="html", reply_markup=markup).id)

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Подобрать другое", callback_data=f"not_at_home_again>{escape(category_name)}>"+"+".join(map(str,messages))),
        InlineKeyboardButton("Выйти в меню", callback_data="menu"),
        row_width=2)
    bot.send_message(call.message.chat.id, "Хотите что то из этого?", reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data.startswith("not_at_home_again>"))
def not_at_home_choose_agina(call: CallbackQuery):
    print(call)
    bot.delete_messages(call.message.chat.id, list(map(int,call.data.split(">")[2].split("+"))))

    not_at_home_choose(call)


@bot.callback_query_handler(func=lambda call: call.data in location_data.keys())
def handle_query(call):
    category = call.data
    genre_menu = create_genre_menu(category)  # Генерация кнопок для жанров
    bot.send_message(call.message.chat.id, "Выберите жанр:", reply_markup=genre_menu)


@bot.callback_query_handler(func=lambda call: '_' in call.data)
def handle_genre(call: CallbackQuery):
    category, genre = call.data.split('_')

    # Здесь добавляем код для добавления/обновления пользователя
    telegram_id = call.message.chat.id

    telegram_username = call.message.from_user.first_name

    # Здесь вы можете настроить значения по умолчанию для новых пользователей
    # Например, если вы хотите, чтобы у пользователя была выбрана категория:
    kino = (category == 'kino')
    concert = (category == 'concert')
    exhibition = (category == 'exhibition')
    excursion = (category == 'excursion')
    theater = (category == 'theater')

    # Добавление пользователя в базу данных
    db.add_user(telegram_id, telegram_username, kino=kino, concert=concert,
                exhibition=exhibition, excursion=excursion, theater=theater)

    # Получаем информацию о фильмах
    movies_info = create_movie_menu(category, genre)  # Получаем информацию о фильмах

    for movie in movies_info:
        # Отправляем фото и описание
        bot.send_photo(
            call.message.chat.id,
            movie["photo"],
            caption=f"{movie['description']}\n[Подробное описание]({movie['link']})",
            parse_mode='Markdown'  # Для Markdown-разметки, чтобы создать ссылку
        )

@bot.callback_query_handler(func=lambda c: c.data == "editprofil")
def editprofil_c(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.send_message(chat_id, "Извините, эта функция еще недоступна. Ожидайте обновлений", reply_markup=main_menu)


if __name__ == '__main__':
    bot.infinity_polling()