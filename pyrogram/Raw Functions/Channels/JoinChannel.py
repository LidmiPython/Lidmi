
from pyrogram.raw.functions.channels import JoinChannel

#Присоединяйтесь к каналу / супергруппе
@app.on_message(message_text_filter(f"123123123"))
async def channels_JoinChannel(client, message):
	msg = await app.send(JoinChannel(channel=await app.resolve_peer(-1001158541073)))
	print(msg)
