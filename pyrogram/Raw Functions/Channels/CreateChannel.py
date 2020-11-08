from pyrogram.raw.functions.channels import CreateChannel
from pyrogram.raw.types import InputGeoPoint

#Создайте супергруппу/канал.
@app.on_message(message_text_filter(f"123123123"))
async def channels_CreateChannel(client, message):
	msg = await app.send(CreateChannel(
		title="test_channels_CreateChannel",
		about="тестовая",))
		#broadcast=True, #если True Создайте канал (optional)
		#megagroup=True, #если True Создайте супергруппу (optional)
		#geo_point=InputGeoPoint(lat=float, long=float), #Расположение группы (optional)
		#address="бла Бла Бла")) #Адрес геогруппы (optional)
	print(msg)
