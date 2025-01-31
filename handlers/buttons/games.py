from aiogram import Router, types, F

rt_games = Router()

@rt_games.callback_query(F.data == "games")
async def game(callback: types.CallbackQuery) -> None:

    
    await callback.message.edit_reply_markup(reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[
        types.InlineKeyboardButton(text="❌Крестики нолики🔵", callback_data="tic_tac_toe")
    ]]))


