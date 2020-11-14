from pyrogram.raw.functions.messages import GetDialogUnreadMarks
#Получить диалоги, помеченные вручную как непрочитанные
@app.on_message()
async def messages_GetDialogUnreadMarks(client, message):
	msg = await app.send(GetDialogUnreadMarks())
	print(msg)
