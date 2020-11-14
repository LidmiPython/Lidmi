from pyrogram.raw.functions.messages import EditChatAdmin
#Сделайте пользователя администратором в устаревшей группе .
@app.on_message(message_text_filter(f"123123123"))
async def messages_EditChatAdmin(client, message):
	msg = await app.send(EditChatAdmin(chat_id=428336336,
		user_id=await app.resolve_peer(1265322007),
		is_admin=True)
		)
	print(msg)