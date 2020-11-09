from pyrogram.raw.functions.channels import DeleteHistory

#Удалить историю супергруппы.
@app.on_message()
async def channels_DeleteHistory(client, message):
	msg = await app.send(DeleteHistory(
		channel=await app.resolve_peer(-1001158541073),
		max_id=1))
	print(msg)
