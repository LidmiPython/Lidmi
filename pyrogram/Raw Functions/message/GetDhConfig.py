from pyrogram.raw.functions.messages import GetDhConfig
#ПВозвращает параметры конфигурации для генерации ключа Диффи-Хеллмана. Может также возвращать случайную последовательность байтов требуемой длины.
@app.on_message()
async def messages_GetDhConfig(client, message):
	msg = await app.send(GetDhConfig(version=0,
		random_length=0))
	print(msg)
