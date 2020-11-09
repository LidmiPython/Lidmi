from pyrogram.raw.functions.channels import ReadHistory

#Отметить историю канала / супергруппы как прочитанную
@app.on_message()
async def channels_LeaveChannel(client, message):
	msg = await app.send(ReadHistory(channel=await app.resolve_peer(-1001158541073),
		max_id=2978))
	print(msg)
