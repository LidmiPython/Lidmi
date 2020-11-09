from pyrogram.raw.functions.channels import GetFullChannel

#Получить полную информацию о канале
@app.on_message(message_text_filter(f"123123123"))
async def channels_GetFullChannel(client, message):
	msg = await app.send(GetFullChannel(
		channel=await app.resolve_peer(-1001322182991)))
	print(msg)
