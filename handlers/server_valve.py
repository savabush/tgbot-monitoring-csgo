# Aiogram
from aiogram import types, Dispatcher
import os

# Api
from valve_api.info_server import get_info_server_csgo


async def info_server(msg: types.Message):
    server_address = (os.getenv('SERVER_IP'), int(os.getenv('SERVER_PORT')))
    server_info = get_info_server_csgo(server_address)
    await msg.answer(server_info)


def register_handler_valve(dp: Dispatcher):
    dp.register_message_handler(info_server, lambda msg: msg.text == 'Информация и статус')