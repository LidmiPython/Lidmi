from pyrogram.raw.functions.messages import DeleteScheduledMessages
#Удалить запланированные сообщения
@app.on_message()
async def messages_DeleteScheduledMessages(client, message):
	msg = await app.send(DeleteScheduledMessages(peer=await app.resolve_peer(),
		id=[1])
		)
	print(msg)
