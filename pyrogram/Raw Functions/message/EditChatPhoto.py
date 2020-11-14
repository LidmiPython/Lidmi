from pyrogram.raw.functions.messages import EditChatPhoto
from pyrogram.raw.types import InputChatUploadedPhoto
#Меняет фото чата и отправляет на нем служебное сообщение
@app.on_message(message_text_filter(f"123123123"))
async def messages_EditChatPhoto(client, message):
	file_id_upl = await app.save_file("/home/suslik/Рабочий стол/photo_2020-11-04_18-13-21.jpg")
	msg = await app.send(EditChatPhoto(chat_id=440539810,
		photo=InputChatUploadedPhoto(file=file_id_upl)))
	print(msg)