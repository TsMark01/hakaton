from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import location_data



# Главная клавиатура
main_menu = InlineKeyboardMarkup()
main_menu.add(
    InlineKeyboardButton("👨‍👩‍👧 Семья", callback_data="family:edit"),
    row_width=1
)
main_menu.add(
    InlineKeyboardButton("🎉 Подобрать досуг", callback_data="main_leisure"),
    InlineKeyboardButton("📜 Инструкция", callback_data="instruction"),
    row_width=2
)
main_menu.add(
    InlineKeyboardButton("✏️ Редактировать профиль", callback_data="editprofil"),
    InlineKeyboardButton("🏡 Выйти в меню", callback_data="family"),
    row_width=1
)

# Клавиатура выбора досуга
main_leisure = InlineKeyboardMarkup()
main_leisure.add(
    InlineKeyboardButton("🏠 Дома", callback_data="at_home"),
    InlineKeyboardButton("🚶‍♀️ Не дома", callback_data="not_at_home")
)

# Клавиатура для получения активности
markup_get_activity = InlineKeyboardMarkup()
markup_get_activity.add(
    InlineKeyboardButton("🔍 Подобрать еще активность", callback_data="at_home"),
    InlineKeyboardButton("🏠 Выйти в меню", callback_data="family"),
    row_width=1
)

def create_genre_menu(category):
    genre_menu = InlineKeyboardMarkup()
    for genre in location_data[category].keys():
        genre_menu.add(InlineKeyboardButton(genre.capitalize(), callback_data=f"{category}_{genre}"))
    return genre_menu

# Функция для создания меню фильмов
# Функция для создания меню с фильмами (концертами)
def create_movie_menu(category, genre):
    movies_info = []  # Список для хранения информации о фильмах
    for movie_id, movie_info in location_data[category][genre].items():
        # Форматирование информации о каждом фильме
        movie_details = {
            "photo": movie_info[0],  # Ссылка на изображение
            "description": movie_info[1],  # Описание фильма (или концерта)
            "link": movie_info[2],  # Ссылка на подробности
        }
        movies_info.append(movie_details)  # Добавляем информацию о фильме в список

    return movies_info  # Возвращаем список с информацией о фильмах

interests_markup = InlineKeyboardMarkup()
for category in location_data.keys():
    interests_markup.add(InlineKeyboardButton(category.capitalize(), callback_data=category))
