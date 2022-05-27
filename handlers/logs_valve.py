# Aiogram
from aiogram import types, Dispatcher

# Api
from valve_api.logs.logs_server import get_logs_server
from valve_api.logs.logs_console import get_logs_console


async def logs_server(msg: types.Message):
    result = get_logs_server()
    await msg.answer(result)


async def logs_console(msg: types.Message):
    result = get_logs_console()
    await msg.answer(result)


def register_handler_logs_valve(dp: Dispatcher):
    dp.register_message_handler(logs_server, lambda msg: msg.text == 'Логи сервера')
    dp.register_message_handler(logs_console, lambda msg: msg.text == 'Логи консоли')
