from pyrogram.raw.functions.channels import ToggleSlowMode

#Переключить медленный режим супергруппы: если этот параметр включен, пользователи смогут отправлять только одно сообщение каждую seconds секунду
@app.on_message()
async def channels_ToggleSlowMode(client, message):
	msg = await app.send(ToggleSlowMode(channel=await app.resolve_peer(-1001158541073),
			seconds=10))
