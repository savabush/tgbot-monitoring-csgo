# Aiogram
from aiogram import types, Dispatcher

# Api
from valve_api.logs.logs_server import get_logs_server
from valve_api.logs.logs_console import get_logs_console
from valve_api.logs.logs_script import get_logs_script
from valve_api.logs.logs_metamod import get_logs_metamod
from valve_api.logs.logs_sourcemod import get_logs_sourcemod


async def logs_server(msg: types.Message):
    result = get_logs_server()
    await msg.answer(result)


async def logs_console(msg: types.Message):
    result = get_logs_console()
    await msg.answer(result)


async def logs_script(msg: types.Message):
    result = get_logs_script()
    await msg.answer(result)


async def logs_metamod(msg: types.Message):
    result = get_logs_metamod()
    await msg.answer(result)


async def logs_sourcemod(msg: types.Message):
    result = get_logs_sourcemod()
    await msg.answer(result)


def register_handler_logs_valve(dp: Dispatcher):
    dp.register_message_handler(logs_server, lambda msg: msg.text == 'Логи сервера')
    dp.register_message_handler(logs_console, lambda msg: msg.text == 'Логи консоли')
    dp.register_message_handler(logs_script, lambda msg: msg.text == 'Логи скрипта')
    dp.register_message_handler(logs_metamod, lambda msg: msg.text == 'Логи MetaMod')
    dp.register_message_handler(logs_sourcemod, lambda msg: msg.text == 'Логи SourceMod')
