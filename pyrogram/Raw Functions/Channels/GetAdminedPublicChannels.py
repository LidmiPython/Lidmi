from pyrogram.raw.functions.channels import GetAdminedPublicChannels

#Получить каналы / супергруппы / геогруппы, в которых мы администрируем. \
# Обычно вызывается, когда пользователь превышает предел для собственных общедоступных (каналов/супергрупп/геогрупп) , \
# и пользователю предоставляется выбор удалить один из его (каналов/супергрупп/геогрупп).
@app.on_message(message_text_filter(f"123123123"))
async def channels_GetAdminedPublicChannels(client, message):
	msg = await app.send(GetAdminedPublicChannels(
		by_location=True, # (optional) 
		check_limit=True, # (optional) 
	))
	print(msg)
