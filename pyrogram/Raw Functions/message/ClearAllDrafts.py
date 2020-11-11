from pyrogram.raw.functions.messages import ClearAllDrafts
#Очистить все Черновики .
@app.on_message()
async def messages_ClearAllDrafts(client, message):
	msg = await app.send(ClearAllDrafts())
	print(msg)
