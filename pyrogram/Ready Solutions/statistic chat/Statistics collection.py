from pyrogram import filters
import sqlite3
from loguru import logger as logg

def message_text_filter(text):
    async def func(flt, _, msg):
        return flt.data == msg.text

    return filters.create(func, data=text)

@app.on_message(message_text_filter(f"statistic_chat") & filters.me)
async def Statistics_collection(client, message):
    namebd = f"basa_data/statistic_chat_test.db"
    conn = sqlite3.connect(namebd)  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS stata (
        chat_id    TEXT,
        user_id    TEXT,
        first_name TEXT,
        last_name  TEXT,
        count      INT,
        rang       TEXT)""")
    try:
        chat_id = int(str(message.chat.id).replace("-", ''))
        name1 = cursor.execute("""SELECT chat_id,message_id FROM one_message WHERE chat_id=?""", (chat_id,)).fetchone()
        async for message in app.iter_history(-int(name1[0]), offset_id=int(name1[1]),reverse = False):
            if message.from_user:
                chat_id = str(message.chat.id).replace("-", '')
                logg.info(f"msg_id=({message.message_id}), user_id=({message.from_user.id}), first_name=({message.from_user.first_name}), chat_id=({message.chat.id}), text=({message.text})")
                user_id = message.from_user.id
                user_first_name = message.from_user.first_name
                user_last_name = message.from_user.last_name
                name1 = cursor.execute("""SELECT chat_id ,user_id FROM stata WHERE user_id=? and chat_id=?""",
                                       (user_id, chat_id,)).fetchone()
                if name1 == None:
                    cursor.execute("""INSERT INTO stata (chat_id, user_id, first_name, last_name, count, rang) VALUES(?,?,?,?,"1","чайник");""", (str(chat_id),str(user_id), user_first_name, user_last_name,))
                else:
                    cursor.execute("""UPDATE stata set "count" = "count" + 1 WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    name2 = cursor.execute("""SELECT count FROM stata WHERE user_id=? and chat_id=?""", (user_id,chat_id,)).fetchone()
                    if name2[0] == 6:
                        cursor.execute("""UPDATE stata set "rang"="Рядовой"             WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 33:
                        cursor.execute("""UPDATE stata set "rang"="Ефрейтор"            WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 100:
                        cursor.execute("""UPDATE stata set "rang"="Капрал"              WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 246:
                        cursor.execute("""UPDATE stata set "rang"="Мастер-капрал"       WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 473:
                        cursor.execute("""UPDATE stata set "rang"="«Сержант»"           WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 820:
                        cursor.execute("""UPDATE stata set "rang"="Штаб-сержант"        WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 1333:
                        cursor.execute("""UPDATE stata set "rang"="Мастер-сержант"      WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 1933:
                        cursor.execute("""UPDATE stata set "rang"="«Первый сержант»"    WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 2773:
                        cursor.execute("""UPDATE stata set "rang"="«Сержант-майор»"     WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 3800:
                        cursor.execute("""UPDATE stata set "rang"="«Уорэнт-офицер 1»"   WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 5066:
                        cursor.execute("""UPDATE stata set "rang"="«Уорэнт-офицер 2»"   WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 6533:
                        cursor.execute("""UPDATE stata set "rang"="«Уорэнт-офицер 3»"   WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 8333:
                        cursor.execute("""UPDATE stata set "rang"="«Уорэнт-офицер 4»"   WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 10400:
                        cursor.execute("""UPDATE stata set "rang"="«Уорэнт-офицер 5»"   WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 12800:
                        cursor.execute("""UPDATE stata set "rang"="«Младший лейтенант»" WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 15533:
                        cursor.execute("""UPDATE stata set "rang"="«Лейтенант»"         WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 18666:
                        cursor.execute("""UPDATE stata set "rang"="«Старший лейтенант»" WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 22133:
                        cursor.execute("""UPDATE stata set "rang"="«Капитан»"           WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 26000:
                        cursor.execute("""UPDATE stata set "rang"="«Майор»"             WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 29666:
                        cursor.execute("""UPDATE stata set "rang"="«Подполковник»"      WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 35133:
                        cursor.execute("""UPDATE stata set "rang"="«Полковник»"         WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 40400:
                        cursor.execute("""UPDATE stata set "rang"="«Бригадир»"          WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 46133:
                        cursor.execute("""UPDATE stata set "rang"="«Генерал-майор»"     WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 52466:
                        cursor.execute("""UPDATE stata set "rang"="«Генерал-лейтенант»" WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 59226:
                        cursor.execute("""UPDATE stata set "rang"="«Генерал»"           WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 66666:
                        cursor.execute("""UPDATE stata set "rang"="«Маршал»"            WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 74800:
                        cursor.execute("""UPDATE stata set "rang"="«Фельдмаршал»"       WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 81666:
                        cursor.execute("""UPDATE stata set "rang"="«Командор»"          WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 93333:
                        cursor.execute("""UPDATE stata set "rang"="«Генералиссимус»"    WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
                    elif name2[0] == 100000:
                        cursor.execute("""UPDATE stata set "rang"="«Легенда»"           WHERE user_id=? and chat_id=?""", (user_id,chat_id,))
            else:
                print("сообщение не от user, не идут в учет, Сорри")
    finally:
        conn.commit()
        conn.close()