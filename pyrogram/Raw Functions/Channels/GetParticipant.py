from pyrogram.raw.functions.channels import GetParticipant

@app.on_message()
async def channels_GetParticipant(client, message):
	msg = await app.send(GetParticipant(
		channel=await app.resolve_peer(-1001158541073),
		user_id=await app.resolve_peer(1398764450)))
	print(msg)
