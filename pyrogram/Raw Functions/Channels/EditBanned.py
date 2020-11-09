from pyrogram.raw.functions.channels import EditBanned
from pyrogram.raw.types import ChatBannedRights

#Забанить / разблокировать / кикнуть пользователя в супергруппе / канале.
@app.on_message()
async def channels_EditBanned(client, message):
	msg = await app.send(EditBanned(
		channel=await app.resolve_peer(-1001158541073),
		user_id=await app.resolve_peer(495741541),
		banned_rights=ChatBannedRights(until_date=60*5,
									view_messages=False,
									send_messages=False,
									send_media=False,
									send_stickers=False,
									send_gifs=False,
									send_games=False,
									send_inline=False,
									embed_links=False,
									send_polls=False,
									change_info=False,
									invite_users=False,
									pin_messages=False,
)))
	print(msg)
