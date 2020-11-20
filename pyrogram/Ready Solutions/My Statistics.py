from pyrogram import filters
import sqlite3


def message_text_filter(text):
    async def func(flt, _, msg):
        return flt.data == msg.text

    return filters.create(func, data=text)

@app.on_message(message_text_filter(f"my_stata") & filters.me)
def my_statistic(client, message):
    namebd = f"basa_data/statistic_chat.db"
    conn = sqlite3.connect(namebd)  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    user_id = message.from_user.id
    chat_id = str(message.chat.id).replace("-", '')
    top_count = cursor.execute(f"""SELECT chat_id,user_id,first_name, count, rang FROM stata WHERE user_id=? and chat_id=?""", (user_id,chat_id,)).fetchall()
    print(top_count)
    top = [f'Имя = [{top_count[2]}](tg://user?id={top_count[1]})',
           f'колл сообщений {top_count[3]}',
           f'ранг = {top_count[4]}']
    app.send_message(message.chat.id, "\n".join(top))