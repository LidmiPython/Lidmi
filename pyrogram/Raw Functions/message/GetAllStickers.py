from pyrogram.raw.functions.messages import GetAllStickers
#Получите все установленные стикеры
@app.on_message()
async def messages_GetAllStickers(client, message):
	msg = await app.send(GetAllStickers(hash=0))
	print(msg)