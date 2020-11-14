from pyrogram.raw.functions.messages import GetChats
#Возвращает основную информацию чата об их идентификаторах.
@app.on_message()
async def messages_GetChats(client, message):
	msg = await app.send(GetChats(id=[440539810]))
	print(msg)