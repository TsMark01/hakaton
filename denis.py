from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from telebot.util import escape
from schema import *

def unescape(text: str) -> str: return text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")

from bot import bot
from db import db
import keyboard

# Временные списки членов семей - dict[<Id семьи>, dist[<Имя члена семьи>, <Инфо Члена семьи>]]
tempMembersList: dict[int, dict[str, MemberData]] = {}

@bot.callback_query_handler(func=lambda c: c.data == "family")
def familyMenu(call: CallbackQuery):
    bot.edit_message_text("Перевожу в меню...", call.message.chat.id, call.message.id, reply_markup=keyboard.main_menu)

# Редактирование семьи
@bot.callback_query_handler(func=lambda c: c.data == "family:edit")
def familyEditMenu(call: CallbackQuery):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Добавить члена семьи ➕", callback_data="family:member:create"),
        InlineKeyboardButton("Список членов семьи 👨‍👨‍👦‍👦", callback_data="family:member:list"),
        InlineKeyboardButton("« Назад", callback_data="family"),
        row_width=1)

    bot.edit_message_text("Редактор семьи", call.message.chat.id, call.message.id, reply_markup=markup)  # TODO


# Иницилизация списка членов семьи
@bot.callback_query_handler(func=lambda c: c.data == ("family:member:list"))
def familyMembersList(call: CallbackQuery):
    # Получаем членов семьи
    l = db.get_family_members_by_telegram_id(call.from_user.id)
    # Очищаем и сохраняем во временный словарь по Id семьи
    tempMembersList[call.from_user.id] = {}
    for i in l: tempMembersList[call.from_user.id][i.name] = i

    familyMembersListMenu(call)  # Открываем меню со страницами


# Список членов семьи по страницам r"family:member:list>(\d++)"
@bot.callback_query_handler(func=lambda c: c.data.startswith("family:member:list>"))
def familyMembersListMenu(call: CallbackQuery):
    try:
        page = int(call.data.split(">")[1])  # Получаем страницу
    except:
        page = 0

    if not call.from_user.id in tempMembersList:
        return familyEditMenu(call)  # except: Если списка небыло во временном словаре
    members = tuple(tempMembersList[call.from_user.id].values())  # Получаем из словаря значения
    display = members[page * 6:page * 6 + 6]  # Берём 6 записей по страницам

    markup = InlineKeyboardMarkup()
    markup.add(
        *[InlineKeyboardButton(d.name, callback_data=f"family:member:edit>{escape(d.name)}") for d in display],
        row_width=2)
    markup.add(
        (InlineKeyboardButton("🠔 Назад", callback_data=f"family:member:list>{page - 1}")
         if page > 0 else InlineKeyboardButton("« Назад", callback_data="family:edit")),
        # Если страница 1-я, возвращяем к редактору семьи
        row_width=1)
    if (len(members) > 6):  # Если есть ещё страницы
        markup.add(
            (InlineKeyboardButton("Вперёд ➝", callback_data=f"family:member:list>{page + 1}")
             if page * 6 + 5 < len(members) else InlineKeyboardButton("« В начало",
                                                                      callback_data="family:member:list>0")),
            # Кнопка 'В начало' если страница последняя
            row_width=2)

    bot.edit_message_text(f"Список членов семьи\nСтраница {page + 1}/{(len(members) + 5) // 6}", call.message.chat.id,
                          call.message.id, reply_markup=markup)  # TODO


# Редатирование члена семьи r"family:member:list>(\w++)"
@bot.callback_query_handler(func=lambda c: c.data.startswith("family:member:edit>"))
def familyMemberEditMenu(call: CallbackQuery):
    member: MemberData = db.get_family_member_by_name(call.from_user.id, unescape(call.data.split(">")[1]))

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Удалить ❌", callback_data=f"family:member:delete>{escape(member.name)}"),
        InlineKeyboardButton("« Назад", callback_data="family:member:list"),
        row_width=1)

    bot.edit_message_text(f"{member.name}\n{member.age} лет", call.message.chat.id, call.message.id,
                          reply_markup=markup)


# Добавление члена семьи... Вопрос имени
@bot.callback_query_handler(func=lambda c: c.data == "family:member:create")
def familyMemberCreate(call: CallbackQuery):
    message = bot.edit_message_text("Ведите имя", call.message.chat.id, call.message.id,
                                    reply_markup=InlineKeyboardMarkup())
    # Передаём в callback последнее сообщение для его редактирования
    bot.register_next_step_handler(message, lambda m: memberCreateAcceptName(m, message))


# Добавление члена семьи... Вопрос возвраста
def memberCreateAcceptName(message: Message, prevMessage: Message):
    # message - сообщение пользователя
    # prevMessage - полследние сообщение бота

    name = message.text
    bot.delete_message(message.chat.id, message.id)
    bot.edit_message_text(f"Каков возвраст <b>{escape(name)}</b>", prevMessage.chat.id, prevMessage.id,
                          parse_mode="html")
    # Передаём в callback последнее сообщение для его редактирования, и имя
    bot.register_next_step_handler(prevMessage, lambda m: memberCreateAcceptAge(m, prevMessage, name))


# Добавление члена семьи... Вопрос роли
def memberCreateAcceptAge(message: Message, prevMessage: Message, name: str):
    # message - сообщение пользователя
    # prevMessage - полследние сообщение бота

    bot.delete_message(message.chat.id, message.id)
    try:
        age = int(message.text)
    except:  # Если не удалось распасить возвраст (не число), переспрос
        message = bot.edit_message_text("Не удалось понять возраст\nВведите возвраст заново", prevMessage.chat.id,
                                        prevMessage.id)
        bot.register_next_step_handler(message, lambda m: memberCreateAcceptAge(m, prevMessage, name))
        return

    if age < 0:  # Если не допустимое значение, переспрос
        message = bot.edit_message_text("Спустись на землю\nВведите возвраст заново", prevMessage.chat.id,
                                        prevMessage.id)
        bot.register_next_step_handler(message, lambda m: memberCreateAcceptAge(m, prevMessage, name))
        return

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Родитель 👨", callback_data=f"family:member:create:data>{escape(name)}>{age}>parent"),
        InlineKeyboardButton("👶 Ребёнок", callback_data=f"family:member:create:data>{escape(name)}>{age}>child"),
        row_width=2)
    message = bot.edit_message_text(f"Какова роль <b>{escape(name)}</b> в семье", prevMessage.chat.id, prevMessage.id,
                                    parse_mode="html", reply_markup=markup)


# Добавление члена семьи r"family:member:create:data>(?<name>\w++)>(?<age>\d++)>(?<role>\w++)"
@bot.callback_query_handler(func=lambda c: c.data.startswith("family:member:create:data>"))
def memberCreateAcceptRole(call: CallbackQuery):
    try:
        # Из callback-а берём дату
        data = call.data.split(">")
        member = MemberData(unescape(data[1]), int(data[2]), data[3] == "parent")
    except:
        # Что-то пошло нетак? - в редактор семьи
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("« Назад", callback_data="family:edit"), row_width=1)
        bot.edit_message_text("Произошла ошибка 🤷‍♂️", reply_markup=markup)
        return

    # Добавляем
    db.add_family_member(call.from_user.id, member.name, member.age, member.role)

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("« К семье", callback_data="family:edit"), row_width=1)
    bot.edit_message_text(f"<b>{member.name}</b> добавлен в семью", call.message.chat.id, call.message.id,
                          parse_mode="html", reply_markup=markup)


# Удаление члена семьи r"family:member:create:data>(?<name>\w++)"
@bot.callback_query_handler(func=lambda c: c.data.startswith("family:member:delete>"))
def familyMemberDelete(call: CallbackQuery):
    member: str = unescape(call.data.split(">")[1])
    db.delete_family_member_by_name(call.from_user.id, member)
    del tempMembersList[call.from_user.id][member]

    return familyEditMenu(call, call.from_user)