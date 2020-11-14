from pyrogram.raw.functions.messages import EditMessage
#Редактировать сообщение
@app.on_message()
async def messages_EditMessage(client, message):
	msg = await app.send(EditMessage(peer=await app.resolve_peer(1398764450),
		id=14942,
		message="NOT NOT NOT"))
	print(msg)