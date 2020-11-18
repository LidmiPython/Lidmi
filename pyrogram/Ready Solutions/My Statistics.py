from pyrogram import filters
import sqlite3


def message_text_filter(text):
    async def func(flt, _, msg):
        return flt.data == msg.text

    return filters.create(func, data=text)

@app.on_message(message_text_filter(f"my_stata") & filters.me)
def static_chat(client, message):
    namebd = f"basa_data/static_chat.db"
    conn = sqlite3.connect(namebd)  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    user_id = message.from_user.id
    top_count = cursor.execute("""SELECT first_name, id, count, rang FROM TXT3 WHERE id=?""", (user_id,)).fetchone()
    top = [f'Имя = [{top_count[0]}](tg://user?id={top_count[1]})',
           f'колл сообщений `{top_count[2]}`',
           f'ранг = `{top_count[3]}`']
    app.send_message(message.chat.id, "\n".join(top))