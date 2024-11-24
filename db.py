import sqlite3

# Создаем или открываем базу данных
conn = sqlite3.connect('user_preferences.db')

# Создаем курсор
cursor = conn.cursor()

# Создаем таблицу для хранения пользовательских предпочтений
cursor.execute('''
CREATE TABLE IF NOT EXISTS user_preferences (
    user_id INTEGER PRIMARY KEY,
    selected_categories TEXT
)
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()


def add_user_preferences(user_id, selected_category):
    conn = sqlite3.connect('user_preferences.db')
    cursor = conn.cursor()

    # Проверяем, существует ли уже пользователь
    cursor.execute('SELECT selected_categories FROM user_preferences WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()

    if result:
        # Если пользователь существует, обновляем его предпочтения
        current_preferences = result[0]
        # Добавляем новую категорию, если её там нет
        if selected_category not in current_preferences:
            selected_preferences = current_preferences + ',' + selected_category
            cursor.execute('UPDATE user_preferences SET selected_categories = ? WHERE user_id = ?',
                           (selected_preferences, user_id))
    else:
        # Если пользователь не существует, создаем новую запись
        cursor.execute('INSERT INTO user_preferences (user_id, selected_categories) VALUES (?, ?)',
                       (user_id, selected_category))

    conn.commit()
    conn.close()


def get_user_preferences(user_id):
    conn = sqlite3.connect('user_preferences.db')
    cursor = conn.cursor()

    # Получаем предпочтения пользователя
    cursor.execute('SELECT selected_categories FROM user_preferences WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0].split(',')
    else:
        return []

import sqlite3
from sqlite3 import Error
import os

db_file_path = os.getenv('DB_FILE_PATH', 'bot_database.db')


import sqlite3
from sqlite3 import Error
import os
from schema import *

db_file_path = os.getenv('DB_FILE_PATH', 'bot_database.db')


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        user_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE,
            telegram_username TEXT,
            kino BOOLEAN DEFAULT FALSE,
            concert BOOLEAN DEFAULT FALSE,
            exhibition BOOLEAN DEFAULT FALSE,
            excursion BOOLEAN DEFAULT FALSE,
            theater BOOLEAN DEFAULT FALSE,
            kino_genre TEXT,
            concert_genre TEXT,
            theater_theme TEXT,
            exhibition_theme TEXT,
            excursion_theme TEXT
        );
        """

        family_query = """
        CREATE TABLE IF NOT EXISTS family (
            telegram_id INTEGER NOT NULL,
            member_name TEXT NOT NULL,
            member_age INTEGER NOT NULL,
            member_role BOOLEAN,
            PRIMARY KEY (telegram_id, member_name)
        );
        """

        try:
            with self.connection:
                self.connection.execute(user_query)
                self.connection.execute(family_query)
        except Error as e:
            print(f"An error occurred while creating tables: {e}")

    def close(self):
        self.connection.close()

    # Functions for working with users
    def get_user_by_telegram_id(self, telegram_id):
        query = "SELECT * FROM users WHERE telegram_id = ?"
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, (telegram_id,))
            return cursor.fetchone()

    def add_user(self, telegram_id, telegram_username):
        query = "INSERT OR IGNORE INTO users (telegram_id, telegram_username) VALUES (?, ?)"
        with self.connection:
            self.connection.execute(query, (telegram_id, telegram_username))

    # Functions for working with family
    def get_family_members_by_telegram_id(self, telegram_id):
        query = "SELECT member_name, member_age, member_role FROM family WHERE telegram_id = ?"
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, (telegram_id,))
            return [MemberData(i[0], i[1], i[2]) for i in cursor.fetchall()]

    def add_family_member(self, telegram_id, member_name, member_age, member_role):
        query = "INSERT INTO family (telegram_id, member_name, member_age, member_role) VALUES (?, ?, ?, ?)"
        with self.connection:
            self.connection.execute(query, (telegram_id, member_name, member_age, member_role))

    def update_family_member(self, telegram_id, member_name, member_age=None, member_role=None):
        updates = []
        if member_age is not None:
            updates.append("member_age = ?")
        if member_role is not None:
            updates.append("member_role = ?")

        if updates:
            update_query = f"UPDATE family SET {', '.join(updates)} WHERE telegram_id = ? AND member_name = ?"
            params = [v for v in (member_age, member_role) if v is not None]
            params.append(telegram_id)
            params.append(member_name)
            with self.connection:
                self.connection.execute(update_query, params)

    def delete_family_member(self, telegram_id, member_name):
        query = "DELETE FROM family WHERE telegram_id = ? AND member_name = ?"
        with self.connection:
            self.connection.execute(query, (telegram_id, member_name))

db = Database(db_file_path)