from pyrogram.raw.functions.channels import GetInactiveChannels

#Получите неактивные каналы и супергруппы
@app.on_message()
async def channels_GetAdminedPublicChannels(client, message):
	msg = await app.send(GetInactiveChannels())
	print(msg)
