from pyrogram.raw.functions.channels import GetFullChannel

#Получить полную информацию о канале
@app.on_message()
async def channels_GetFullChannel(client, message):
	msg = await app.send(GetFullChannel(
		channel=await app.resolve_peer(-1001158541073)))
	print(msg)
