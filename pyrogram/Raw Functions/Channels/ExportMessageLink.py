from pyrogram.raw.functions.channels import ExportMessageLink

#Получить ссылку и вставить информацию о сообщении в канал / супергруппу
@app.on_message()
async def channels_ExportMessageLink(client, message):
	msg = await app.send(ExportMessageLink(
		channel=await app.resolve_peer(-1001158541073),
		id=2894,
		grouped=True))

	print(msg)
	print(msg.link)
	print(msg.html)
