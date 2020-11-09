from pyrogram.raw.functions.channels import SetStickers
from pyrogram.raw.types import InputStickerSetEmpty

#Свяжите набор стикеров с супергруппой
@app.on_message()
async def channels_SetStickers(client, message):
	msg = await app.send(SetStickers(channel=await app.resolve_peer(-1001404882277),
			stickerset=InputStickerSetEmpty()))
	print(msg)
