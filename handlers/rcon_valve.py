# Aiogram
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# Api
from valve_api.rcon.some_command import post_rcon
from valve_api.rcon.users_rcon import get_users_rcon
from valve_api.rcon.kickid_rcon import kick_id

# Keyboards
from keyboards import keyboard_back


class RconState(StatesGroup):
    wait_for_comm = State()
    wait_for_kickid_and_comm = State()


async def some_command(msg: types.Message):
    keyboard = keyboard_back()
    await msg.answer('Введите консольную команду:', reply_markup=keyboard)
    await RconState.wait_for_comm.set()


async def send_some_command(msg: types.Message, state: FSMContext):
    await state.update_data(command=msg.text)
    command = await state.get_data()
    result = post_rcon(command['command'])
    await msg.answer(result)


async def users(msg: types.Message):
    result = get_users_rcon()
    await msg.answer(result)


async def kickid(msg: types.Message):
    result = get_users_rcon()
    users_list = result.split('\n')[9:-3]
    if not users_list:
        await msg.answer('На сервере нет игроков')
        return
    else:
        keyboard = keyboard_back()
        await msg.answer(result)
        await msg.answer('Введите userid игрока и сообщение через пробел:', reply_markup=keyboard)
        await RconState.wait_for_kickid_and_comm.set()


async def send_kickid(msg: types.Message, state: FSMContext):
    text = msg.text.split()
    result = get_users_rcon()
    users_list = result.split('\n')[9:-3]
    if text[0].isdigit() and 0 < int(text[0]) <= len(users_list):
        id_player = text[0]
        message = text[1] if len(text) == 2 else None
        await state.update_data(id_player=id_player, message=message)
        data = await state.get_data()
        result = kick_id(data['id_player'], data['message'])
        await msg.answer(result)
        await state.finish()
    else:
        await msg.answer(result)
        await msg.answer('Введите правильный userid\n\nПример: # 2 --> 1 <-- "username"')
        return


def register_handler_rcon_valve(dp: Dispatcher):
    dp.register_message_handler(users, lambda msg: msg.text == 'Игроки')
    dp.register_message_handler(some_command, lambda msg: msg.text == 'Команда')
    dp.register_message_handler(send_some_command, state=RconState.wait_for_comm)
    dp.register_message_handler(kickid, lambda msg: msg.text == 'Кик')
    dp.register_message_handler(send_kickid, state=RconState.wait_for_kickid_and_comm)
