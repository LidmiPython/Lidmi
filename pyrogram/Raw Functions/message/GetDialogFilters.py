from pyrogram.raw.functions.messages import GetDialogFilters
#Получить папки
@app.on_message(message_text_filter(f"GetDialogFilters"))
async def messages_GetDialogFilters(client, message):
	msg = await app.send(GetDialogFilters())
	print(msg)