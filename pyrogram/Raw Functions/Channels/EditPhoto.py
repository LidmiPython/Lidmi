from pyrogram.raw.functions.channels import EditPhoto
from pyrogram.raw.types import InputChatUploadedPhoto

#Изменить фото канала / супергруппы
@app.on_message()
async def channels_EditPhoto(client, message):
	file_id_upl = await app.save_file("/home/suslik/Рабочий стол/photo_2020-11-04_18-13-21.jpg")
	print(file_id_upl)
	msg = await app.send(EditPhoto(
		channel=await app.resolve_peer(-1001158541073),
		photo=InputChatUploadedPhoto(file=file_id_upl)))
	print(msg)
