from pyrogram.raw.functions.messages import GetDialogFilters
#Получить папки и список чатов в папке
@app.on_message()
async def messages_GetDialogFilters(client, message):
	msg = await app.send(GetDialogFilters())
	print(msg)
