from pyrogram.raw.functions.channels import TogglePreHistoryHidden

#Скрыть / показать историю сообщений для новых пользователей канала / супергруппы
@app.on_message(message_text_filter(f"123123123"))
async def channels_TogglePreHistoryHidden(client, message):
	msg = await app.send(TogglePreHistoryHidden(channel=await app.resolve_peer(-1001158541073),
			enabled=True))
	print(msg)
