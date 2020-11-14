from pyrogram.raw.functions.messages import GetPeerDialogs
from pyrogram.raw.types import InputDialogPeer
#Получить информацию о диалоге указанных пиров
@app.on_message()
async def messages_GetPeerDialogs(client, message):
	msg = await app.send(GetPeerDialogs(peers=[InputDialogPeer(peer=await app.resolve_peer(1398764450))]))
	print(msg)