from pyrogram.raw.functions.channels import GetLeftChannels

#Получите список каналов / супергрупп, которые мы оставили
@app.on_message()
async def channels_GetLeftChannels(client, message):
	msg = await app.send(GetLeftChannels(offset=-1), retries=10, timeout=3.0, sleep_threshold=3.0)
	await asyncio.sleep(3)
	print(msg)
