from pyrogram.raw.functions.channels import ToggleSignatures

#Включение / отключение подписей сообщений в каналах
@app.on_message(message_text_filter(f"123123123"))
async def channels_ToggleSignatures(client, message):
	msg = await app.send(ToggleSignatures(channel=await app.resolve_peer(-1001404882277),
			enabled=True))
	print(msg)
