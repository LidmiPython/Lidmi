from pyrogram.raw.functions.messages import GetArchivedStickers
#Получить все стикеры из архива
@app.on_message()
async def messages_GetArchivedStickers(client, message):
	msg = await app.send(GetArchivedStickers(offset_id=0, limit=0))
	print(msg)