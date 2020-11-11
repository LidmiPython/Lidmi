from pyrogram.raw.functions.messages import DeleteHistory
#Удаляет историю общения
@app.on_message()
async def messages_DeleteHistory(client, message):
	msg = await app.send(DeleteHistory(peer=await app.resolve_peer(),
		max_id=0,
		just_clear=True #(optional)
		))
	print(msg)
