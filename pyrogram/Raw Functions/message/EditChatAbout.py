from pyrogram.raw.functions.messages import EditChatAbout
#Отредактируйте описание (группы / супергруппы / канала ).
@app.on_message()
async def messages_EditChatAbout(client, message):
	msg = await app.send(EditChatAbout(peer=await app.resolve_peer(),
		about="Test")
		)
	print(msg)
