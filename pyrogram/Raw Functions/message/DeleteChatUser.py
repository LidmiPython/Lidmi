from pyrogram.raw.functions.messages import DeleteChatUser
#Удаляет пользователя из чата и отправляет на него служебное сообщение.
@app.on_message()
async def messages_DeleteChatUser(client, message):
	msg = await app.send(DeleteChatUser(chat_id=0, user_id=await app.resolve_peer()))
	print(msg)
