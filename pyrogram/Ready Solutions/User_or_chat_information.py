from pyrogram import filters

def Ver(a):
	if a == True:
		return "✅"
	else:
		return "❌"

def сhat_infor(app, message):
	chat = app.get_chat(message.chat.id)
	msg_count = app.get_history_count(message.chat.id)
	return \
	f"""**чат был проверен Telegram**: `{Ver(chat.is_verified)}`
**чат был ограничен**: `{Ver(chat.is_restricted)}`
**владелец чата**: `{Ver(chat.is_creator)}`
**чат был помечен как мошенничество**: `{Ver(chat.is_scam)}`

**Название**: `{chat.title}`
**@Ник**: `{chat.username}`
**Описание**: `{chat.description}`
**Дата-Центр**: `{chat.dc_id}`
**Название Стикер-Пака**: [{chat.sticker_set_name}](t.me/addstickers/{chat.sticker_set_name})
**Колл Учасников**: `{chat.members_count}`
**общее количество сообщений**: `{msg_count}`"""

def user_infor(app, message):
	if message.chat.type == "private":
		user = app.get_users(message.chat.id)
	elif message.chat.type == "supergroup":
		user = app.get_users(message.reply_to_message.from_user.id)
	return \
	f"""✅ - да, ❌ - нет.
	**являетесь вы сами**: `{Ver(user.is_self)}`
**Находится в ваших контактах**: `{Ver(user.is_contact)}`
**если у вас обоих есть контакт друг с другом.**: `{Ver(user.is_mutual_contact)}`
**этот пользователь удален**: `{Ver(user.is_deleted)}`
**этот пользователь бот**: `{Ver(user.is_bot)}`
**пользователь был проверен Telegram**: `{Ver(user.is_verified)}`
**пользователь был ограничен**: `{Ver(user.is_restricted)}`
**отмечен как мошенник**: `{Ver(user.is_scam)}`
**входит в группу поддержки Telegram**: `{Ver(user.is_support)}`

**id**: `{user.id}`
**имя**: `{user.first_name}`
**фамилия**: `{user.last_name}`
**статус пользователя в сети**: `{user.status}`
**@Ник**: `{user.username}`
**Дата-Центр**: `{user.dc_id}`

[{user.first_name}](tg://user?id={user.id})"""

@app.on_message(filters.command("me", prefixes="!"))
def photo_me(client, message):
	message.delete()
	try:
		x = int(message.text.split('!me ', maxsplit=1)[1]) - 1
	except IndexError:
		x = 0
	if message.reply_to_message:
		if message.chat.type == "private":
			if message.from_user.photo:
				user = app.get_users(message.chat.id)
				app.send_photo(	chat_id=message.chat.id,
							photo=app.get_profile_photos(int(user.id))[x].file_id,
							file_ref=app.get_profile_photos(int(user.id))[x].file_ref,
							caption=f"Фотогрфий: {x + 1} из {app.get_profile_photos_count(message.chat.id)}\n\n" + user_infor(app, message),
							reply_to_message_id=message.reply_to_message.message_id)
			else:
				user = app.get_users(message.chat.id)
				app.send_message(chat_id=message.chat.id, text=f"{user_infor(app, message)}", reply_to_message_id=message.reply_to_message.message_id)
		elif message.chat.type == "supergroup":
			if message.from_user.photo:
				chat = app.get_users(message.reply_to_message.from_user.id)
				print(chat)
				app.send_photo(	chat_id=message.chat.id,
							photo=app.get_profile_photos(int(chat.id))[x].file_id,
							file_ref=app.get_profile_photos(int(chat.id))[x].file_ref,
							caption=f"Фотогрфий: {x + 1} из {app.get_profile_photos_count(chat.id)}\n\n" + user_infor(app, message),
							reply_to_message_id=message.reply_to_message.message_id)
			else:
				chat = app.get_users(message.reply_to_message.from_user.id)
				app.send_message(chat_id=message.chat.id, text=f"{user_infor(app, message)}", reply_to_message_id=message.reply_to_message.message_id)
	else:
		if message.chat.type == "private":
			if message.from_user.photo:
				user = app.get_users(message.chat.id)
				app.send_photo(	chat_id=message.chat.id,
							photo=app.get_profile_photos(int(user.id))[x].file_id,
							file_ref=app.get_profile_photos(int(user.id))[x].file_ref,
							caption=f"Фотогрфий: {x + 1} из {app.get_profile_photos_count(message.chat.id)}\n\n" + user_infor(app, message))
			else:
				user = app.get_users(message.chat.id)
				app.send_message(chat_id=message.chat.id, text=f"{user_infor(app, message)}")
		elif message.chat.type == "supergroup":
			if message.from_user.photo:
				chat = app.get_chat(message.chat.id)
				print(chat)
				app.send_photo(chat_id=message.chat.id,
							photo=app.get_profile_photos(int(chat.id))[x].file_id,
							file_ref=app.get_profile_photos(int(chat.id))[x].file_ref,
							caption=f"Фотогрфий: {x + 1} из {app.get_profile_photos_count(chat.id)}\n\n" + сhat_infor(app, message))
			else:
				chat = app.get_chat(message.chat.id)
				app.send_message(chat_id=message.chat.id, text=f"{сhat_infor(app, message)}")	
