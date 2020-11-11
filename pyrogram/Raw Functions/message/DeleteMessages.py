from pyrogram.raw.functions.messages import DeleteMessages

#Удаляет сообщения по их идентификаторам.
@app.on_message()
async def messages_DeleteMessages(client, message):
	msg = await app.send(DeleteMessages(id=[]))
	print(msg)
