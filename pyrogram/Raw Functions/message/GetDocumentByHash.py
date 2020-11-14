from pyrogram.raw.functions.messages import GetDocumentByHash
#Получить документ по его хешу SHA256, в основном используется для гифок
@app.on_message(message_text_filter(f"GetDocumentByHash"))
async def messages_GetDocumentByHash(client, message):
	msg = await app.send(GetDocumentByHash(Sha256=0,
		size=0,
		mime_type="audio/x-opus+ogg"))
	print(msg)