from pyrogram.raw.functions.channels import GetGroupsForDiscussion

#Получить все группы, которые можно использовать как группы обсуждения.
@app.on_message()
async def channels_GetAdminedPublicChannels(client, message):
	msg = await app.send(GetGroupsForDiscussion())
	print(msg)
