from pyrogram.raw.functions.channels import DeleteMessages

#Удалить сообщения в канале / супергруппе
@app.on_message()
async def channels_DeleteMessages(client, message):
	msg = await app.send(DeleteMessages(
		channel=await app.resolve_peer(-1001158541073),
		id=[2660]))
	print(msg)
