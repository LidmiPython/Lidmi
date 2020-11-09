from pyrogram.raw.functions.channels import GetChannels

#Получить информацию о каналах / супергруппах
@app.on_message()
async def channels_GetChannels(client, message):
	msg = await app.send(GetChannels(
		id=[await app.resolve_peer(-1001158541073)]))
	print(msg)
