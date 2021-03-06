from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as fmt
from keyboards import keyboard_start


async def cmd_start(msg: types.Message, state: FSMContext):
    await state.finish()
    keyboard = keyboard_start()
    await msg.answer('Меню:', reply_markup=keyboard)
    await msg.delete()


async def about(msg: types.Message):
    await msg.answer(f'{fmt.hide_link("github.com/savabush/")}'
                     f'Бот для получения статистики и управления VPS конфигурациями через API Fornex.'
                     f'В этой версии бота также доступен мониторинг серверов Valve.'
                     f'Другие версии этого бота можете посмотреть по ссылке снизу:'
                     f'\n\nMade by savabush', parse_mode=types.ParseMode.HTML)


def register_handler_base(dp: Dispatcher):
    dp.register_message_handler(cmd_start, lambda msg: msg.text == 'Меню' or msg.text == '/start', state='*')
    dp.register_message_handler(about, lambda msg: msg.text == 'О боте')
