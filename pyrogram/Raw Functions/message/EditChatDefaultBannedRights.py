from pyrogram.raw.functions.messages import EditChatDefaultBannedRights
from pyrogram.raw.types import ChatBannedRights
#Отредактируйте заблокированные права по умолчанию для канала / супергруппы / группы .
@app.on_message()
async def messages_EditChatDefaultBannedRights(client, message):
	msg = await app.send(EditChatDefaultBannedRights(peer=await app.resolve_peer(-1001158541073),
		banned_rights=ChatBannedRights(until_date=0,
							view_messages=True,
							send_messages=True,
							send_media=True,
							send_stickers=True,
							send_gifs=True,
							send_games=True,
							send_inline=True,
							embed_links=True,
							send_polls=True,
							change_info=True,
							invite_users=True,
							pin_messages=True))
		)
	print(msg)