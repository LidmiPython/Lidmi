from pyrogram.raw.functions.channels import SetDiscussionGroup

#Свяжите группу с каналом как группу обсуждения для этого канала
@app.on_message()
async def channels_SetDiscussionGroup(client, message):
	msg = await app.send(SetDiscussionGroup(broadcast=await app.resolve_peer(-1001404882277),
			group=await app.resolve_peer(-1001158541073)))
	print(msg)
