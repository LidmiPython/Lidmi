from pyrogram.raw.functions.channels import DeleteChannel

#Удалить канал/супергруппу.
@app.on_message()
async def channels_DeleteChannel(client, message):
	msg = await app.send(DeleteChannel(
		channel=await app.resolve_peer(-1001435500780)))
	print(msg)
