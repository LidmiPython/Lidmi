from pyrogram.raw.functions.channels import ReadMessageContents

#Отметить содержимое сообщения канала / супергруппы как прочитанное
@app.on_message()
async def channels_ReadMessageContents(client, message):
	msg = await app.send(ReadMessageContents(channel=await app.resolve_peer(-1001158541073),
		id=[2978,2927]))
	print(msg)
