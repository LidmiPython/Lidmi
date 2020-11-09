from pyrogram.raw.functions.channels import GetAdminLog
from pyrogram.raw.types import ChannelAdminLogEventsFilter

#Получить журнал администратора канала / супергруппы
@app.on_message()
async def channels_GetAdminLog(client, message):
	msg = await app.send(GetAdminLog(
		channel=await app.resolve_peer(-1001158541073), 
		q="", #Поисковый запрос, может быть пустым
		max_id=0,
		min_id=0,
		limit=0,
		events_filter=ChannelAdminLogEventsFilter(
			join=True,
			leave=True,
			invite=True,
			ban=True,
			unban=True,
			kick=True,
			unkick=True,
			promote=True,
			demote=True,
			info=True,
			settings=True,
			pinned=True,
			edit=True,
			delete=True), # (optional)
		admins=[await app.resolve_peer(1398764450)], # (optional)
	))
	print(msg)
