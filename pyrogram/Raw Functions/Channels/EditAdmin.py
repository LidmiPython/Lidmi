from pyrogram.raw.functions.channels import EditAdmin
from pyrogram.raw.types import ChatAdminRights

#Измените права администратора пользователя в супергруппе / канале .
@app.on_message()
async def channels_EditAdmin(client, message):
	msg = await app.send(EditAdmin(
		channel=await app.resolve_peer(-1001158541073),
		user_id=await app.resolve_peer(1265322007),
		admin_rights=ChatAdminRights(change_info=True,
									post_messages=True,
									edit_messages=True,
									delete_messages=True,
									ban_users=True,
									invite_users=True,
									pin_messages=True,
									add_admins=True),
		rank="ЗамГлАдм"))
	print(msg)
