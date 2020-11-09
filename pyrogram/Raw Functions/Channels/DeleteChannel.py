from pyrogram.raw.functions.channels import DeleteChannel

#Удалить канал/супергруппу.
@app.on_message(message_text_filter(f"123123123"))
async def channels_DeleteChannel(client, message):
	msg = await app.send(DeleteChannel(
		channel=await app.resolve_peer(-1001435500780)))
	print(msg)
