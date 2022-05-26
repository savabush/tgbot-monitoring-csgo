# Aiogram
from aiogram import types, Dispatcher


async def valve_page(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ['Информация и статус', 'Рестарт сервера', 'Включить сервер', 'Выключить сервер']
    keyboard.add(*buttons)
    await msg.answer('Выберите опцию:', reply_markup=keyboard)


def register_handler_valve_page(dp: Dispatcher):
    dp.register_message_handler(valve_page, lambda msg: msg.text == 'Valve')
