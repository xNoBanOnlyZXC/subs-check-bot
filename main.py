import asyncio
from aiogram import Bot, types, Dispatcher
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.command import Command
from config import *

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def create_keyboard(channel_ids):
    keyboard = InlineKeyboardBuilder()
    for channel in channel_ids:
        try:
            title = await bot.get_chat('@'+channel)
            url_button = InlineKeyboardButton(text=title.title, url=f"https://t.me/{channel}")
            keyboard.add(url_button)
        except:
            pass
    keyboard.add(InlineKeyboardButton(text="Проверить подписку", callback_data="check"))
    keyboard.adjust(1)
    return keyboard.as_markup()

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.delete()
    keyboard = await create_keyboard(CHANNEL_IDS)
    await message.answer(welcome_text, reply_markup=keyboard)

@dp.message()
async def check_subscription(message: types.Message):
    user_id = message.from_user.id
    not_subscribed_channels = []
    for channel in CHANNEL_IDS:
        try:
            status = await bot.get_chat_member(chat_id='@'+channel, user_id=user_id)
        except:
            status.status = 'left'
        if status.status == 'left':
            not_subscribed_channels.append(channel)
    await message.delete()
    if not_subscribed_channels:
        await message.answer("Вы не подписались на наши каналы.", reply_markup=create_keyboard(not_subscribed_channels))
    else:
        await message.answer(succ_text)

@dp.callback_query(lambda c: c.data == 'check')
async def call_check_subscription(callback_query: types.CallbackQuery):
    callback_query.answer()
    user_id = callback_query.from_user.id
    not_subscribed_channels = []
    for channel in CHANNEL_IDS:
        try:
            status = await bot.get_chat_member(chat_id='@'+channel, user_id=user_id)
        except:
            status.status = 'left'
        if status.status == 'left':
            not_subscribed_channels.append(channel)
    await callback_query.message.delete()
    if not_subscribed_channels:
        await bot.send_message(callback_query.from_user.id, "Вы не подписались на наши каналы.", reply_markup=create_keyboard(not_subscribed_channels))
    else:
        await bot.send_message(callback_query.from_user.id, succ_text)

if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))