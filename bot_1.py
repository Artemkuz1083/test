import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5468648366:AAFN1A3VR-a_TDaKpnCEYezbpKqrqG7C8QA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(msg: types.Message):
    await msg.reply('Start')


@dp.message_handler(commands=['help'])
async def echo(msg: types.Message):
    await msg.reply('�� ���������� � ������� ����')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)