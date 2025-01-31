from aiogram import Router, types, F
import sqlite3

rt_profile = Router()

@rt_profile.callback_query(F.data == "profile")
async def profile(callback: types.CallbackQuery):
    with sqlite3.connect('database.db') as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT score, money FROM users WHERE id = ?", (callback.from_user.id, ))
        userstat = cursor.fetchone()
    await callback.message.edit_caption(
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[
            types.InlineKeyboardButton(text="◀️Назад", callback_data="back")]]),
        caption=f"🔢Очки: {userstat[0]}\n🪙Монеты: {userstat[1]}")