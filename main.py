from aiogram import Dispatcher, Bot
import asyncio
from setup import config, autosetting; autosetting() #<<<#
from handlers.commands import start
from handlers.buttons import games, profile
from handlers.buttons.lgames import tic_tac_toe

dp = Dispatcher(  )
dp.include_router( start.rt_start )
dp.include_router( games.rt_games )
dp.include_router( tic_tac_toe.rt_tictactoe )
dp.include_router( profile.rt_profile )
bot = Bot(config["token"])

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())