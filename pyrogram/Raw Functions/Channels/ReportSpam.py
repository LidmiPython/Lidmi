from pyrogram.raw.functions.channels import ReportSpam

#Отмечает некоторые сообщения от пользователя в супергруппе как спам; требует прав администратора в супергруппе
@app.on_message()
async def channels_ReportSpam(client, message):
	msg = await app.send(ReportSpam(channel=await app.resolve_peer(-1001158541073),
		user_id=await app.resolve_peer(1349986891),
		id=[2745]))
	print(msg)
