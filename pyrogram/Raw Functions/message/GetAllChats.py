from pyrogram.raw.functions.messages import GetAllChats
#Получите все чаты, каналы и супергруппы
@app.on_message()
async def messages_GetAllChats(client, message):
	msg = await app.send(GetAllChats(
					except_ids=[440539810], #кроме этих
									))
	print(msg)
