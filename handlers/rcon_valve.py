# Aiogram
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# Api
from valve_api.rcon.some_command import post_rcon
from valve_api.rcon.users_rcon import get_users_rcon


class RconState(StatesGroup):
    wait_for_comm = State()


async def some_command(msg: types.Message):
    await msg.answer('Введите консольную команду:')
    await RconState.wait_for_comm.set()


async def send_some_command(msg: types.Message, state: FSMContext):
    await state.update_data(command=msg.text)
    command = await state.get_data()
    result = post_rcon(command['command'])
    await msg.answer(result)
    await state.finish()


async def users(msg: types.Message):
    result = get_users_rcon()
    await msg.answer(result)


def register_handler_rcon_valve(dp: Dispatcher):
    dp.register_message_handler(users, lambda msg: msg.text == 'Игроки')
    dp.register_message_handler(some_command, lambda msg: msg.text == 'Команда')
    dp.register_message_handler(send_some_command, state=RconState.wait_for_comm)
