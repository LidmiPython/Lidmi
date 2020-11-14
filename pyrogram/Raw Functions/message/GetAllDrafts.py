from pyrogram.raw.functions.messages import GetAllDrafts
#Сохранить получить все черновики сообщений .
@app.on_message()
async def messages_GetAllDrafts(client, message):
	msg = await app.send(GetAllDrafts())
	print(msg)
