import sqlite3
from pyrogram import filters


async def send_stat_msg(conn, cursor, message):
    conn.commit()
    top_count = cursor.execute("""SELECT first_name, id, count, rang FROM TXT3 ORDER BY count DESC LIMIT 5""").fetchall()
    top = ["Новый Ранг"
        f'Имя = [{top_count[0][0]}](tg://user?id={top_count[0][1]})',
           f'колл сообщений = `{top_count[0][2]}`',
           f'ранг = `{top_count[0][3]}`']
    await app.send_message(message.chat.id, "\n".join(top))

@app.on_message(filters.chat(-1001432990634))
async def static_chat(client, message):
    namebd = f"basa_data/static_chat_test.db"
    conn = sqlite3.connect(namebd)  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS TXT3 (
        "id"	TEXT,
        "first_name"	TEXT,
        "last_name"	TEXT,
        "count"	INTEGER,
        "rang"	TEXT)""")
    try:
        if message.from_user:
            #https://t.me/GlovoMe/1038775
            user_id = message.from_user.id
            user_first_name = message.from_user.first_name
            user_last_name = message.from_user.last_name
            name1 = cursor.execute(f"""SELECT count(id) FROM TXT3 WHERE id=?""", (user_id,)).fetchone()
            if name1[0]==0:
                cursor.execute("""INSERT INTO TXT3 (id, first_name, last_name, count, rang) VALUES(?,?,?,"1","чайник");""", (user_id, user_first_name, user_last_name,))
            else:
                cursor.execute("""UPDATE TXT3 set "count" = "count" + 1 WHERE id=?""", (user_id,))
                name2 = cursor.execute("""SELECT count FROM TXT3 WHERE id=?""", (user_id,)).fetchone()
                if name2[0] == 6:
                    cursor.execute("""UPDATE TXT3 set "rang"="Рядовой" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 33:
                    cursor.execute("""UPDATE TXT3 set "rang"="Ефрейтор" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 100:
                    cursor.execute("""UPDATE TXT3 set "rang"="Капрал" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 246:
                    cursor.execute("""UPDATE TXT3 set "rang"="Мастер-капрал" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 473:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Сержант»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 820:
                    cursor.execute("""UPDATE TXT3 set "rang"="Штаб-сержант" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 1333:
                    cursor.execute("""UPDATE TXT3 set "rang"="Мастер-сержант" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 1933:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Первый сержант»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 2773:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Сержант-майор»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 3800:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Уорэнт-офицер 1»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 5066:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Уорэнт-офицер 2»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 6533:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Уорэнт-офицер 3»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 8333:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Уорэнт-офицер 4»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 10400:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Уорэнт-офицер 5»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 12800:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Младший лейтенант»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 15533:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Лейтенант»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 18666:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Старший лейтенант»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 22133:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Капитан»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 26000:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Майор»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 29666:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Подполковник»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 35133:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Полковник»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 40400:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Бригадир»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 46133:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Генерал-майор»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 52466:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Генерал-лейтенант»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 59226:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Генерал»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 66666:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Маршал»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 74800:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Фельдмаршал»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 81666:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Командор»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 93333:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Генералиссимус»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
                if name2[0] == 100000:
                    cursor.execute("""UPDATE TXT3 set "rang"="«Легенда»" WHERE id=?""", (user_id,))
                    await send_stat_msg(conn, cursor, message)
        else:
            print("сообщение не от чата, не идут в учет")
    except:
        raise
    finally:
        conn.commit()
