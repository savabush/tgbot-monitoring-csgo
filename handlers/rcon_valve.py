# Aiogram
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# Api
from valve_api.rcon.some_command import post_rcon
from valve_api.rcon.users_rcon import get_users_rcon
from valve_api.rcon.kickid_rcon import kick_id
from valve_api.rcon.banid_rcon import ban_id
from valve_api.rcon.unban_rcon import unban_rcon
from valve_api.rcon.add_vip import add_vip_rcon
from valve_api.rcon.del_vip import del_vip_rcon
from ssh.groups_vip import groups_vip

# Keyboards
from keyboards import keyboard_back


class RconState(StatesGroup):
    wait_for_comm = State()
    wait_for_kickid_and_comm = State()
    wait_for_banid_and_comm = State()
    wait_for_unban = State()
    wait_for_addvip = State()
    wait_for_delvip = State()


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
    if 1 <= len(text) and text[0].isdigit() and 0 < int(text[0]) <= len(users_list):
        id_player = text[0]
        message = ' '.join(text[1:]) if len(text) > 1 else None
        await state.update_data(id_player=id_player, message=message)
        data = await state.get_data()
        result = kick_id(data['id_player'], data['message'])
        await msg.answer(result)
        await state.finish()
    else:
        await msg.answer(result)
        await msg.answer('Введите правильный userid\n\nПример: # 2 --> 1 <-- "username"')
        return


async def banid(msg: types.Message):
    result = get_users_rcon()
    users_list = result.split('\n')[9:-3]
    if not users_list:
        await msg.answer('На сервере нет игроков')
        return
    else:
        keyboard = keyboard_back()
        await msg.answer(result)
        await msg.answer('Введите userid, время бана и сообщение (необязательно) через пробел:', reply_markup=keyboard)
        await RconState.wait_for_banid_and_comm.set()


async def send_banid(msg: types.Message, state: FSMContext):
    text = msg.text.split()
    result = get_users_rcon()
    users_list = result.split('\n')[9:-3]
    if 2 <= len(text) <= 3 and text[0].isdigit() and 0 < int(text[0]) <= len(users_list):
        id_player = text[0]
        time_ban = text[1]
        message = text[2] if len(text) == 3 else None
        await state.update_data(id_player=id_player, time_ban=time_ban, message=message)
        data = await state.get_data()
        result = ban_id(data['id_player'], data['time_ban'], data['message'])
        await msg.answer(result)
        await state.finish()
    else:
        await msg.answer(result)
        await msg.answer('Введите правильный userid и правильное время через пробел\n\nПример: # 2 --> 1 <-- "username"')
        return


async def unban(msg: types.Message):


    keyboard = keyboard_back()
    await msg.answer(banned_users)
    await msg.answer('Введите порядковый номер пользователя:', reply_markup=keyboard)
    await RconState.wait_for_unban.set()


async def send_unban(msg: types.Message, state: FSMContext):

    if 2 <= len(text) <= 3 and text[0].isdigit() and 0 < int(text[0]) <= len(users_list):
        number = msg.text
        await state.update_data(number=number)
        data = await state.get_data()
        result = unban_rcon(data['number'])
        await msg.answer(result)
        await state.finish()
    else:
        await msg.answer(banned_users)
        await msg.answer('Введите правильный номер пользователя')
        return


async def addvip(msg: types.Message):
    result = get_users_rcon()
    users_list = result.split('\n')[9:-3]
    groups = groups_vip()
    groups_list = '\n'.join(f'{i} - {group}' for i, group in enumerate(groups, 1))
    if not users_list:
        await msg.answer('На сервере нет игроков')
        return
    else:
        keyboard = keyboard_back()
        await msg.answer(result)
        await msg.answer(groups_list)
        await msg.answer('Введите userid игрока, номер группы и время в секундах через пробел:', reply_markup=keyboard)
        await RconState.wait_for_addvip.set()


async def send_addvip(msg: types.Message, state: FSMContext):
    text = msg.text.split()
    result = get_users_rcon()
    users_list = result.split('\n')[9:-3]
    groups = groups_vip()
    groups_list = '\n'.join(f'{i} - {group}' for i, group in enumerate(groups, 1))
    if len(text) == 3 and all(x.isdigit() for x in text) \
            and 0 < int(text[1]) <= len(groups) and 0 < int(text[0]) <= len(users_list):
        id_player = text[0]
        group_number = text[1]
        time_vip = text[2]
        await state.update_data(id_player=id_player, group_number=group_number, time_vip=time_vip)
        data = await state.get_data()
        result = add_vip_rcon(data['id_player'], data['group_number'], data['time_vip'])
        await msg.answer(result)
        await state.finish()
    else:
        await msg.answer(result)
        await msg.answer(groups_list)
        await msg.answer('Введите правильный userid и номер группы\n\nПример userid: # 2 --> 1 <-- "username"')
        return


async def delvip(msg: types.Message):
    result = get_users_rcon()
    users_list = result.split('\n')[9:-3]
    if not users_list:
        await msg.answer('На сервере нет игроков')
        return
    else:
        keyboard = keyboard_back()
        await msg.answer(result)
        await msg.answer('Введите userid игрока:', reply_markup=keyboard)
        await RconState.wait_for_delvip.set()


async def send_delvip(msg: types.Message, state: FSMContext):
    text = msg.text
    result = get_users_rcon()
    users_list = result.split('\n')[9:-3]
    if text.isdigit() and 0 < int(text) <= len(users_list):
        await state.update_data(id_player=text)
        data = await state.get_data()
        result = del_vip_rcon(data['id_player'])
        await msg.answer(result)
        await state.finish()
    else:
        await msg.answer(result)
        await msg.answer('Введите правильный userid\n\nПример userid: # 2 --> 1 <-- "username"')
        return


def register_handler_rcon_valve(dp: Dispatcher):
    dp.register_message_handler(users, lambda msg: msg.text == 'Игроки')
    dp.register_message_handler(some_command, lambda msg: msg.text == 'Команда')
    dp.register_message_handler(send_some_command, state=RconState.wait_for_comm)
    dp.register_message_handler(kickid, lambda msg: msg.text == 'Кик')
    dp.register_message_handler(send_kickid, state=RconState.wait_for_kickid_and_comm)
    dp.register_message_handler(banid, lambda msg: msg.text == 'Бан')
    dp.register_message_handler(send_banid, state=RconState.wait_for_banid_and_comm)
    dp.register_message_handler(unban, lambda msg: msg.text == 'Убрать из бана')
    dp.register_message_handler(send_unban, state=RconState.wait_for_unban)
    dp.register_message_handler(addvip, lambda msg: msg.text == 'Добавить VIP')
    dp.register_message_handler(send_addvip, state=RconState.wait_for_addvip)
    dp.register_message_handler(delvip, lambda msg: msg.text == 'Удалить VIP')
    dp.register_message_handler(send_delvip, state=RconState.wait_for_delvip)
