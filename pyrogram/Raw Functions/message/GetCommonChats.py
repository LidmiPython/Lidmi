from pyrogram.raw.functions.messages import GetCommonChats
#Получить общие чаты
@app.on_message()
async def messages_GetCommonChats(client, message):
	msg = await app.send(GetCommonChats(user_id=await app.resolve_peer(495741541),
		max_id=999999,
		limit=100))
	print(msg)
