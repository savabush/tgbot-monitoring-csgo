# Aiogram
from aiogram import types, Dispatcher
from keyboards import keyboard_valve_page


async def valve_page(msg: types.Message):
    keyboard = keyboard_valve_page()
    await msg.answer('Выберите опцию:', reply_markup=keyboard)


def register_handler_valve_page(dp: Dispatcher):
    dp.register_message_handler(valve_page, lambda msg: msg.text == 'Valve')
