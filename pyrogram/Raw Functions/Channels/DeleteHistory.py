from pyrogram.raw.functions.channels import DeleteHistory

#Удалить историю супергруппы.
@app.on_message(message_text_filter(f"123123123"))
async def channels_DeleteChannel(client, message):
	msg = await app.send(DeleteHistory(
		channel=await app.resolve_peer(-1001322182991),
		max_id=1))
	print(msg)
