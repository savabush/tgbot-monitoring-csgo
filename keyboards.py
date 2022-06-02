from aiogram import types


def keyboard_start():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = ['Valve', 'О боте']
    keyboard.add(*buttons)
    return keyboard


def keyboard_valve_page():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ['Информация и статус', 'Рестарт сервера', 'Включить сервер',
               'Выключить сервер', 'Логи', 'RCON', 'Меню']
    keyboard.add(*buttons)
    return keyboard


def keyboard_logs_menu():
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = ['Логи сервера', 'Логи консоли', 'Логи скрипта',
               'Логи SourceMod', 'Логи MetaMod', 'Меню']
    keyboard.add(*buttons)
    return keyboard


def keyboard_rcon_menu():
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = ['Игроки', 'Кик', 'Бан', 'Убрать из бана', 'Добавить VIP', 'Удалить VIP', 'Команда', 'Меню']
    keyboard.add(*buttons)
    return keyboard


def keyboard_back():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ['Назад']
    keyboard.add(*buttons)
    return keyboard
