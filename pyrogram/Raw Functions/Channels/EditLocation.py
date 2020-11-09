from pyrogram.raw.functions.channels import EditLocation
from pyrogram.raw.types import InputGeoPointEmpty

#Изменить местоположение геогруппы
@app.on_message()
async def channels_EditLocation(client, message):
	msg = await app.send(EditLocation(
		channel=await app.resolve_peer(-1001158541073),
		geo_point=InputGeoPointEmpty(),
		address="тут какой-то адресс"))
	print(msg)
