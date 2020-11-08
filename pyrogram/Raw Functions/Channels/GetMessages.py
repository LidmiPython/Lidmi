from pyrogram.raw.types import InputMessageID
from pyrogram.raw.functions.channels import GetMessages

@app.on_message()
async def channels_GetMessages(client, message):
	msg = await app.send(GetMessages(
		channel=await app.resolve_peer(-1001158541073),
		id=[InputMessageID(id=1)]))
	print(msg)
