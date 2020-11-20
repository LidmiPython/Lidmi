from pyrogram import filters
import sqlite3


def message_text_filter(text):
    async def func(flt, _, msg):
        return flt.data == msg.text

    return filters.create(func, data=text)

@app.on_message(message_text_filter(f"TOP5") & filters.me)
def static_chat(client, message):
    chat_id = str(message.chat.id).replace("-", '')
    namebd = f"basa_data/statistic_chat.db"
    conn = sqlite3.connect(namebd)  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    top_count = cursor.execute(
        """SELECT chat_id,user_id,first_name, count, rang FROM stata WHERE chat_id=? ORDER BY count DESC""",
        (chat_id,)).fetchall()
    top = ['Самый активные учасники чата',
           "",
           f'Имя = [{top_count[0][2]}](tg://user?id={top_count[0][1]})',
           f'колл сообщений {top_count[0][3]}',
           f'ранг = {top_count[0][4]}',
           '',
           f'Имя = [{top_count[1][2]}](tg://user?id={top_count[1][1]})',
           f'колл сообщений {top_count[1][3]}',
           f'ранг = {top_count[1][4]}',
           '',
           f'Имя = [{top_count[2][2]}](tg://user?id={top_count[2][1]})',
           f'колл сообщений {top_count[2][3]}',
           f'ранг = {top_count[2][4]}',
           '',
           f'Имя = [{top_count[3][2]}](tg://user?id={top_count[3][1]})',
           f'колл сообщений {top_count[3][3]}',
           f'ранг = {top_count[3][4]}',
           '',
           f'Имя = [{top_count[4][2]}](tg://user?id={top_count[4][1]})',
           f'колл сообщений {top_count[4][3]}',
           f'ранг = {top_count[4][4]}',
           '']
    app.send_message(message.chat.id, "\n".join(top))