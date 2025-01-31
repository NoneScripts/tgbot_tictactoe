from aiogram import Router, filters, types, F
import sqlite3

rt_start = Router()
async def get_inline() -> list[types.InlineKeyboardButton]:
    return [[types.InlineKeyboardButton(text="🎮Игры", callback_data="games")],
            [types.InlineKeyboardButton(text="👨‍🦰Профиль", callback_data="profile")]]

@rt_start.message(filters.CommandStart())
async def start(msg: types.Message):

    with sqlite3.connect("database.db") as connect:
        cursor = connect.cursor()
        cursor.execute("INSERT OR IGNORE INTO users (id, score, money) VALUES (?, ?, ?)", (msg.from_user.id, 0, 100))
        connect.commit()
    await msg.answer_photo(reply_markup=types.InlineKeyboardMarkup(inline_keyboard=await get_inline()),
                            photo=types.FSInputFile("handlers/commands/sprites/preview.png"),
                            caption="Выберите действие")

@rt_start.callback_query(F.data == "back")
async def back(callback: types.CallbackQuery):
    await callback.message.edit_caption(
        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=await get_inline()),
        caption="Выберите действие"                     
    )