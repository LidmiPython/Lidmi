from pyrogram.raw.functions.messages import ExportChatInvite
#Экспорт ссылки для приглашения в чат
@app.on_message(message_text_filter(f"123123123"))
async def messages_ExportChatInvite(client, message):
	msg = await app.send(ExportChatInvite(peer=await app.resolve_peer(-440539810)))
	print(msg.link)