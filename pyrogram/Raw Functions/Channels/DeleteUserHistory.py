from pyrogram.raw.functions.channels import DeleteUserHistory

#Удалить все сообщения, отправленные определенным пользователем в супергруппе
@app.on_message()
async def channels_DeleteUserHistory(client, message):
	msg = await app.send(DeleteUserHistory(
		channel=await app.resolve_peer(-1001158541073),
		user_id=await app.resolve_peer(1077524548)))
	print(msg)
