from pyrogram.raw.functions.messages import EditChatTitle
#Меняет имя чата и отправляет на него служебное сообщение.
@app.on_message()
async def messages_EditChatTitle(client, message):
	file_id_upl = await app.save_file("/home/suslik/Рабочий стол/photo_2020-11-04_18-13-21.jpg")
	msg = await app.send(EditChatTitle(chat_id=440539810,
		title="Updsdsd"))
	print(msg)