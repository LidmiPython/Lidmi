from pyrogram.raw.functions.messages import ForwardMessages
#Пересылает сообщения по их идентификаторам.
@app.on_message()
async def messages_ForwardMessages(client, message):
	msg = await app.send(ForwardMessages(from_peer=await app.resolve_peer(-1001158541073), #c какого чата
		id=[2985],
		random_id=[3642865],
		to_peer=await app.resolve_peer(1265322007) #в какой чата
		))
	print(msg)