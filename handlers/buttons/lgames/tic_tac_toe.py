from aiogram import Router, filters, types, F
from aiogram.fsm.context import FSMContext
import sqlite3
import random


rt_tictactoe = Router()
COMBO_WIN = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]           ]

@rt_tictactoe.callback_query(F.data == "tic_tac_toe")
async def initgame(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(field=["n"] * 9)
    await tic_tac_toe(callback, state)

async def tic_tac_toe(callback: types.CallbackQuery, state: FSMContext):
    rows_ttt = [[], [], []]
    index = 0
    field = await state.get_data()
    for i, t_t_t in enumerate(field["field"], 1):
        if t_t_t == 'n':
            rows_ttt[index] += [types.InlineKeyboardButton(text="  ", callback_data=f"p_{i}")]
        elif t_t_t == 'x':
            rows_ttt[index] += [types.InlineKeyboardButton(text="❌", callback_data=f"p_{i}")]
        elif t_t_t == 'o':
            rows_ttt[index] += [types.InlineKeyboardButton(text="🔵", callback_data=f"p_{i}")]
            
        if i % 3 == 0:
            index += 1
        if index == 3:
            break

    await callback.message.edit_reply_markup(reply_markup=types.InlineKeyboardMarkup(inline_keyboard=rows_ttt))

async def check_win(callback: types.CallbackQuery, state: FSMContext):
    field = await state.get_data()
    field = field["field"]
    
    for combo_x in COMBO_WIN:
        if field[combo_x[0]] == "x" and field[combo_x[1]] == 'x' and field[combo_x[2]] == 'x':
            with sqlite3.connect("database.db") as connect:
                cursor = connect.cursor()
                cursor.execute("UPDATE users SET score = score + ? WHERE id = ?", (15, callback.from_user.id))
                connect.commit()

            await callback.message.edit_caption(caption="❌ Крестики победили! + 15 score",
                                                reply_markup=types.InlineKeyboardMarkup(inline_keyboard=
                                                    [[types.InlineKeyboardButton(text="🔄Ещё раз", callback_data="tic_tac_toe")],
                                                    [types.InlineKeyboardButton(text="◀️Назад", callback_data="back")]]
                                                ))
            await state.clear()
            return
    for combo_x in COMBO_WIN:
        if field[combo_x[0]] == "o" and field[combo_x[1]] == 'o' and field[combo_x[2]] == 'o':
            await callback.message.edit_caption(caption="🔵 нолики победили(",
                                                reply_markup=types.InlineKeyboardMarkup(inline_keyboard=
                                                    [[types.InlineKeyboardButton(text="🔄Ещё раз", callback_data="tic_tac_toe")],
                                                    [types.InlineKeyboardButton(text="◀️Назад", callback_data="back")]]
                                                ))
            await state.clear()
            return
    i = 0
    for f in field:
        if "n" != f:
            i += 1
    if i == 9:
        await callback.message.edit_caption(caption="❔ничья, никто не победил",
                                                reply_markup=types.InlineKeyboardMarkup(inline_keyboard=
                                                    [[types.InlineKeyboardButton(text="🔄Ещё раз", callback_data="tic_tac_toe")],
                                                    [types.InlineKeyboardButton(text="◀️Назад", callback_data="back")]]
                                                ))
        await state.clear()

async def bot_set(callback: types.CallbackQuery, state: FSMContext, field: list, index_element: int) -> None:
    field[int(index_element)] = 'o'
    await state.update_data(field=field)
    await tic_tac_toe(callback, state)
    await check_win(callback, state)

async def bot_find(field: list) -> int:
    for i, f in enumerate(field):
            if f == 'o':
                return i
async def bot_set_random(callback: types.CallbackQuery, state: FSMContext, field: list) -> None:
    while True:
            index_element = random.randint(0, 8)
            field = await state.get_data()
            field = field["field"]
            if not field[index_element] in ['x', 'o']:       
                await bot_set(callback, state, field, index_element)
                break
async def bot_protect(callback: types.CallbackQuery, state: FSMContext, field: list, a: int, b: int, c: int) -> bool:
    """
    Where a - index 1\n
    Where b - index 2\n
    Where c - index 3\n
    """
    for combo_x in COMBO_WIN:
        if field[combo_x[a]] == "x" and field[combo_x[b]] == 'x':
            if not field[combo_x[c]] == "o":
                await bot_set(callback, state, field, combo_x[c])

                return True
    
async def bot(callback: types.CallbackQuery, state: FSMContext):

    field = await state.get_data()
    field = field["field"]

    if await bot_protect(callback, state, field, 0, 1, 2):
        return
    if await bot_protect(callback, state, field, 2, 1, 0):
        return
    if await bot_protect(callback, state, field, 0, 2, 1):
        return
    

    
    if not "o" in field:
        if "x" != field[4]:
            await bot_set(callback, state, field, 4)
        else:
            await bot_set_random(callback, state, field)
    else:
        position = await bot_find(field)
        NB = [[1, 3, 4], [0, 2, 3, 4, 5], [1, 4, 5],
              [0, 1, 4, 7, 6], [0, 1, 2, 3, 5, 6, 7, 8], [1, 2, 4, 7, 8],
              [3, 4, 7], [6, 3, 4, 5, 8], [7, 4, 5]]
        free_pos = []
        for pos in NB[position]:
            if not field[pos] in ['x', 'o']:
                free_pos += [pos]
                
                
        else:
            if len(free_pos) > 0:
                await bot_set(callback, state, field, random.choice(free_pos))
            else:
                await bot_set_random(callback, state, field)


        #0 #1 #2
        #3 #4 #5
        #6 #7 #8

@rt_tictactoe.callback_query(F.data.startswith("p_"))
async def player(callback: types.CallbackQuery, state: FSMContext):
    index_element = int(callback.data.split("_")[1]) - 1
    field = await state.get_data()
    field = field["field"]
    
    if not field[index_element] in ['x', 'o']:       
        field[index_element] = 'x'
        await state.update_data(field=field)
        await check_win(callback, state)
        await bot(callback, state)

