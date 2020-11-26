from pyrogram import filters
from time_setup.SETUP import DATES_SETUP # Импорт класса

bts = DATES_SETUP() # Обьявление класса

@app.on_message(filters.me, group=-1)
def ls(client, message):
	await app.send_message(message.chat.id ,f"{bts.bot_runned()}") # Сколько работает программа

if __name__ == '__main__':
	bts.reset_date() # Обновление или сборс времени
	app.run()
