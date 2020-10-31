import pyrogram

app = Client("session_name",
             api_id=******,
             api_hash="******",
             lang_code="ru")

@app.on_message(message_text_filter(f"test2435346456453464565675675465476567567"))
async def test_send_message(client, message):
  await app.send_message(message.chat.id, f'''тестовое сообщение''')#отправить сообщение в чат
  await app.send_message(message.from_user.id, f'''тестовое сообщение''')#отправить сообщение юзеру
