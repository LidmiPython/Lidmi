from pyrogram.raw.functions.channels import CheckUsername

#Проверьте, является ли имя пользователя свободным и может ли быть назначено каналу/супергруппе
@app.on_message()
async def channels_CheckUsername(client, message):
	msg = await app.send(CheckUsername(
		channel=await app.resolve_peer(-1001158541073),
		username="Juxepes"))
	print(msg)
