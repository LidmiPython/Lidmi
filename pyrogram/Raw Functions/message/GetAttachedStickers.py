from pyrogram.raw.functions.messages import GetAttachedStickers
from pyrogram.raw.types import InputPhotoEmpty
from pyrogram.raw.types import InputStickeredMediaPhoto
#Прикрепите стикеры к фото или видео
@app.on_message()
async def messages_GetAttachedStickers(client, message):
	msg = await app.send(GetAttachedStickers(media=InputStickeredMediaPhoto(id=InputPhotoEmpty())))
	print(msg)