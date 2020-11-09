from pyrogram.raw.functions.channels import LeaveChannel

#Покинуть канал / супергруппу
@app.on_message()
async def channels_LeaveChannel(client, message):
	msg = await app.send(LeaveChannel(channel=await app.resolve_peer(-1001158541073)))
	print(msg)
