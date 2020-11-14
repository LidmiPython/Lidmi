from pyrogram.raw.functions.messages import FaveSticker
from pyrogram.raw.types import InputDocumentEmpty
#Отметить стикер как избранный
@app.on_message()
async def messages_FaveSticker(client, message):
	msg = await app.send(FaveSticker(id=InputDocumentEmpty(), unfave=True))
	print(msg)