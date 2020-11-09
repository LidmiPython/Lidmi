from pyrogram.raw.functions.channels import UpdateUsername

#Изменить имя пользователя супергруппы / канала
@app.on_message()
async def channels_UpdateUsername(client, message):
	msg = await app.send(UpdateUsername(channel=await app.resolve_peer(-1001158541073),
			username="Python_help_newbie"))
	print(msg)
