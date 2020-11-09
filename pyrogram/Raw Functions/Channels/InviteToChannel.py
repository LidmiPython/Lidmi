from pyrogram.raw.functions.channels import InviteToChannel

#Пригласить пользователей в канал / супергруппу
@app.on_message()
async def channels_InviteToChannel(client, message):
	msg = await app.send(InviteToChannel(channel=await app.resolve_peer(-1001158541073),
		users=[await app.resolve_peer(123123123)]))
	print(msg)
