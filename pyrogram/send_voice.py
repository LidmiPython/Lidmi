import pyrogram

app = Client("session_name",
             api_id=******,
             api_hash="******",
             lang_code="ru")

@app.on_message()
async def test_send_voice(client, message):
  voice = '1DirectedbyRobertWeide.ogg'
  await app.send_voice(message.chat.id, voice)# отправить войс в чат
  await app.send_voice(message.from_user.id, voice)# отправить войс юзеру

  await app.send_voice(message.chat.id, voice, reply_to_message_id=message.reply_to_message.message_id)# отправить в чат и Ответитив на сообщение, используя его идентификатор
  await app.send_voice(message.from_user.id, voice, reply_to_message_id=message.reply_to_message.message_id)# отправить войс юзеру и Ответитив на сообщение, используя его идентификатор
  
  await app.send_voice(message.chat.id, voice, caption="voice note")# отправить войс в чат и Добавть подпись к голосовому сообщению
  await app.send_voice(message.from_user.id, voice, caption="voice note")# отправить войс юзеру и Добавть подпись к голосовому сообщению

  await app.send_voice(message.chat.id, voice,, reply_to_message_id=message.reply_to_message.message_id, caption="voice note")# отправить войс в чат и Ответитив на сообщение, используя его идентификатор и Добавть подпись к голосовому сообщению
  await app.send_voice(message.from_user.id, voice,, reply_to_message_id=message.reply_to_message.message_id, caption="voice note")# отправить войс юзеру и Ответитив на сообщение, используя его идентификатор и Добавть подпись к голосовому сообщению
