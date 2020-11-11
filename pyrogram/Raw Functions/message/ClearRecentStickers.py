from pyrogram.raw.functions.messages import ClearRecentStickers
#Удалить недавние стикеры
@app.on_message()
async def messages_ClearRecentStickers(client, message):
	msg = await app.send(ClearRecentStickers())
	print(msg)