import pyrogram

app = Client("session_name",
             api_id=******,
             api_hash="******",
             lang_code="ru")

@app.on_message()
async def test_send_voice(client, message):
  voice = '1DirectedbyRobertWeide.ogg
  await app.send_voice(message.chat.id, voice, reply_to_message_id=message.reply_to_message.message_id)# отправить в чат и ответить на сообщение на которое вы ответили
  await app.send_voice(message.chat.id, voice)# отправить войс в чат

  await app.send_voice(message.from_user.id, voice, reply_to_message_id=message.reply_to_message.message_id)# отправить войс юзеру и ответить на сообщение на которое вы ответили
  await app.send_voice(message.from_user.id, voice)# отправить войс юзеру
