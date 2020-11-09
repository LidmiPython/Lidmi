from pyrogram.raw.functions.channels import EditTitle

#Редактировать название канала / супергруппы
@app.on_message()
async def channels_EditTitle(client, message):
	msg = await app.send(EditTitle(
		channel=await app.resolve_peer(-1001158541073),
		title="Новички Python"))
	print(msg)
