import pyrogram

app = Client("session_name",
             api_id=******,
             api_hash="******",
             lang_code="ru")

@app.on_message()
async def test_send_message(client, message):
  await app.send_message(message.chat.id, f'''тестовое сообщение''')#отправить сообщение в чат
  await app.send_message(message.from_user.id, f'''тестовое сообщение''')#отправить сообщение юзеру
  
  await app.send_message(message.chat.id, f'''тестовое сообщение''', disable_web_page_preview=True)#отправить сообщение в чат без предварительного предосмотра веб страницы
  await app.send_message(message.from_user.id, f'''тестовое сообщение''', disable_web_page_preview=True)#отправить сообщение юзеру без предварительного предосмотра веб страниц
  
  await app.send_message(message.chat.id, f'''тестовое сообщение''', reply_to_message_id=message.reply_to_message.message_id)#отправить сообщение в чат Ответитив на сообщение, используя его идентификатор
  await app.send_message(message.from_user.id, f'''тестовое сообщение''', reply_to_message_id=message.reply_to_message.message_id)#отправить сообщение юзеру Ответитив на сообщение, используя его идентификатор
