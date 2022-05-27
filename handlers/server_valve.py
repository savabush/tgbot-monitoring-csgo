# Aiogram
from aiogram import types, Dispatcher

# Api
from valve_api.info_server import get_info_server_csgo
from valve_api.restart_server import restart_server_ssh
from valve_api.turn_on_server import turn_on_server_ssh
from valve_api.turn_off_server import turn_off_server_ssh


async def logs_menu(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = ['Логи сервера', 'Логи консоли', 'Логи скрипта',
               'Логи SourceMod', 'Логи MetaMod', 'Меню']
    keyboard.add(*buttons)
    await msg.answer('Выберите опцию:', reply_markup=keyboard)


async def rcon_menu(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = ['Игроки', 'Кик', 'Бан', 'Убрать из бана', 'Добавить админа',
               'Удалить админа', 'Добавить VIP', 'Удалить VIP', 'Команда', 'Меню']
    keyboard.add(*buttons)
    await msg.answer('Выберите опцию:', reply_markup=keyboard)


async def info_server_ssh(msg: types.Message):
    server_info = get_info_server_csgo()
    await msg.answer(server_info)


async def restart_server(msg: types.Message):
    result = restart_server_ssh()
    await msg.answer(result)


async def turn_on_server(msg: types.Message):
    result = turn_on_server_ssh()
    await msg.answer(result)


async def turn_off_server(msg: types.Message):
    result = turn_off_server_ssh()
    await msg.answer(result)


def register_handler_valve(dp: Dispatcher):
    dp.register_message_handler(info_server_ssh, lambda msg: msg.text == 'Информация и статус')
    dp.register_message_handler(restart_server, lambda msg: msg.text == 'Рестарт сервера')
    dp.register_message_handler(turn_on_server, lambda msg: msg.text == 'Включить сервер')
    dp.register_message_handler(turn_off_server, lambda msg: msg.text == 'Выключить сервер')
    dp.register_message_handler(rcon_menu, lambda msg: msg.text == 'RCON')
    dp.register_message_handler(logs_menu, lambda msg: msg.text == 'Логи')
