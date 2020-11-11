from pyrogram.raw.functions.messages import CreateChat
#Создает новый чат.
@app.on_message()
async def messages_CreateChat(client, message):
	msg = await app.send(CreateChat(users=[await app.resolve_peer()],
		title="кто там ?"))
	print(msg)
