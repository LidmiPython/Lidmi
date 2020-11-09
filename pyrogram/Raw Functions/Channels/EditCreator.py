from pyrogram.raw.functions.channels import EditCreator
from pyrogram.raw.types import InputCheckPasswordEmpty

#Передать право собственности на канал
@app.on_message()
async def channels_EditCreator(client, message):
	msg = await app.send(EditCreator(
		channel=await app.resolve_peer(-1001158541073),
		user_id=await app.resolve_peer(1265322007),
		password=InputCheckPasswordEmpty()))
	print(msg)
