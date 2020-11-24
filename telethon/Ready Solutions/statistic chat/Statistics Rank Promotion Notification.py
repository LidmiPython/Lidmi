from telethon import TelegramClient, events
from telethon.utils import get_display_name

@bot.on(events.NewMessage)
async def Statistics_Rank_Promotion_Notification(message):
    try:
        namebd = f"basa_data/statistic_chat1.db"
        conn = sqlite3.connect(namebd, isolation_level=None)  # или :memory: чтобы сохранить в RAM
        cursor = conn.cursor()
        cursor.execute('PRAGMA synchronous = 0')
        cursor.execute('PRAGMA journal_mode = OFF')
        cursor.execute('PRAGMA temp_store = MEMORY')
        cursor.execute("PRAGMA cache_size = 200000")
        cursor.execute("begin")
        cursor.executescript("""CREATE TABLE IF NOT EXISTS stata (
            chat_id    INT,
            user_id    INT,
            first_name TEXT,
            last_name  TEXT,
            count      INT,
            rang       TEXT
        );
    
        CREATE TABLE IF NOT EXISTS one_message (
            chat_id    INT,
            message_id INT
        );
    
        CREATE TABLE IF NOT EXISTS alls (
            alls_msg    INT,
            alls_chang    INT
        );""")
        try:
            try:
                chat_id = int(str(message.chat_id).replace("-", ''))
                user_id = message.id
                name1 = cursor.execute("""SELECT count(chat_id) FROM one_message WHERE chat_id=?""", (chat_id,)).fetchone()
                if name1[0] == 0:
                    cursor.execute("""INSERT INTO one_message (chat_id ,message_id) VALUES(?,?);""", (chat_id, user_id,))
                else:
                    pass
            except:
                raise

            if message.is_group:
                if message:
                    if message.sender_id:
                        #logg.info(f"user_id=({message.sender_id}), chat_id=({message.chat_id})")
                        user_id = message.sender_id
                        sender = await message.get_sender()
                        user_first_name = sender.first_name
                        user_last_name = sender.last_name
                        print(user_first_name)
                        print(user_last_name)
                        chat_id = int(str(message.chat_id).replace("-", ''))
                        name1 = cursor.execute("""SELECT chat_id ,user_id FROM stata WHERE user_id=? and chat_id=?""",
                                               (user_id, chat_id,)).fetchone()
                        try:
                            if name1 == None:
                                cursor.execute(
                                    """INSERT INTO stata (chat_id ,user_id, first_name, last_name, count, rang) VALUES(?,?,?,?,"1","чайник");""",
                                    (chat_id, user_id, user_first_name, user_last_name,))
                            else:
                                cursor.execute("""UPDATE stata set "count" = "count" + 1 WHERE user_id=? and chat_id=?""",
                                               (user_id, chat_id,))
                        except Exception as e:
                            raise
                        name2 = cursor.execute("""SELECT count FROM stata WHERE user_id=? and chat_id=?""",
                                               (user_id, chat_id,)).fetchone()
                        if name2[0] == 3:
                            cursor.execute("""UPDATE stata set "rang"="«Рядовой»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            #await send_stat_msg(user_id, chat_id, cursor, conn, app, message)
                        elif name2[0] == 33:
                            cursor.execute("""UPDATE stata set "rang"="«Ефрейтор»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            #await send_stat_msg(user_id, chat_id, cursor, conn, app, message)
                        elif name2[0] == 100:
                            cursor.execute("""UPDATE stata set "rang"="«Капрал»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            #await send_stat_msg(user_id, chat_id, cursor, conn, app, message)
                        elif name2[0] == 246:
                            cursor.execute("""UPDATE stata set "rang"="«Мастер-капрал»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            #await send_stat_msg(user_id, chat_id, cursor, conn, app, message)
                        elif name2[0] == 473:
                            cursor.execute("""UPDATE stata set "rang"="«Сержант»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            #await send_stat_msg(user_id, chat_id, cursor, conn, app, message)
                        elif name2[0] == 820:
                            cursor.execute(f"""UPDATE stata set "rang"="«Штаб-сержант»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            #await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 1333:
                            cursor.execute(f"""UPDATE stata set "rang"="«Мастер-сержант»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            #await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 1933:
                            cursor.execute(f"""UPDATE stata set "rang"="«Первый сержант»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            #await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 2773:
                            cursor.execute(f"""UPDATE stata set "rang"="«Сержант-майор»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            #await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 3800:
                            cursor.execute(f"""UPDATE stata set "rang"="«Уорэнт-офицер 1»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            #await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 5066:
                            cursor.execute(f"""UPDATE stata set "rang"="«Уорэнт-офицер 2»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 6533:
                            cursor.execute(f"""UPDATE stata set "rang"="«Уорэнт-офицер 3»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 8333:
                            cursor.execute(f"""UPDATE stata set "rang"="«Уорэнт-офицер 4»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 10400:
                            cursor.execute(f"""UPDATE stata set "rang"="«Уорэнт-офицер 5»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 12800:
                            cursor.execute(f"""UPDATE stata set "rang"="«Младший лейтенант»" WHERE user_id=? and chat_id=?""",
                                            (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 15533:
                            cursor.execute(f"""UPDATE stata set "rang"="«Лейтенант»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 18666:
                            cursor.execute(f"""UPDATE stata set "rang"="«Старший лейтенант»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 22133:
                            cursor.execute(f"""UPDATE stata set "rang"="«Капитан»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 26000:
                            cursor.execute(f"""UPDATE stata set "rang"="«Майор»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 29666:
                            cursor.execute(f"""UPDATE stata set "rang"="«Подполковник»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 35133:
                            cursor.execute(f"""UPDATE stata set "rang"="«Полковник»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 40400:
                            cursor.execute(f"""UPDATE stata set "rang"="«Бригадир»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 46133:
                            cursor.execute(f"""UPDATE stata set "rang"="«Генерал-майор»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 52466:
                            cursor.execute(f"""UPDATE stata set "rang"="«Генерал-лейтенант»" WHERE user_id=? and chat_id=?""",
                                            (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 59226:
                            cursor.execute(f"""UPDATE stata set "rang"="«Генерал»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 66666:
                            cursor.execute(f"""UPDATE stata set "rang"="«Маршал»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 74800:
                            cursor.execute(f"""UPDATE stata set "rang"="«Фельдмаршал»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 81666:
                            cursor.execute(f"""UPDATE stata set "rang"="«Командор»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 93333:
                            cursor.execute(f"""UPDATE stata set "rang"="«Генералиссимус»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                        elif name2[0] == 100000:
                            cursor.execute(f"""UPDATE stata set "rang"="«Легенда»" WHERE user_id=? and chat_id=?""",
                                           (user_id, chat_id,))
                            await send_stat_msg(user_id, chat_id, cursor, app, message)
                    else:
                        print("сообщение не от user, не идут в учет, Сорри")
                elif message.new_chat_members:
                    print("сообщение о 'новом учаснике чата', не идут в учет, Сорри")
                elif message.left_chat_member:
                    print("сообщение о 'удален из группы', не идут в учет, Сорри")
                elif message.new_chat_title:
                    print("сообщение о 'заголовок чата был изменен', не идут в учет, Сорри")
                elif message.new_chat_photo:
                    print("сообщение 'фото чата было изменено', не идут в учет, Сорри")
                elif message.delete_chat_photo:
                    print("сообщение 'фото чата удалено', не идут в учет, Сорри")
                elif message.group_chat_created:
                    print("сообщение ' группа создана', не идут в учет, Сорри")
                elif message.supergroup_chat_created:
                    print("сообщение 'супергруппа создана', не идут в учет, Сорри")
                elif message.channel_chat_created:
                    print("сообщение 'канал создан', не идут в учет, Сорри")
                elif message.migrate_to_chat_id:
                    print("сообщение 'группа была перенесена в супергруппу', не идут в учет, Сорри")
                elif message.migrate_from_chat_id:
                    print(
                        "сообщение 'cупергруппа была перенесена из группы с указанным идентификатором', не идут в учет, Сорри")
                elif message.pinned_message:
                    print("сообщение 'указанное сообщение закреплено', не идут в учет, Сорри")
                elif message.service:
                    print("сообщение 'является служебным', не идут в учет, Сорри")
                elif message.empty:
                    print("сообщение 'пустое', не идут в учет, Сорри")
        except:
            raise
        finally:
            ttt = conn.total_changes
            name1 = cursor.execute("""SELECT alls_msg, alls_chang FROM alls""").fetchone()
            if name1 == None:
                cursor.execute("""INSERT INTO alls (alls_msg, alls_chang) VALUES(1, 1);""")
            else:
                cursor.execute(f"""UPDATE alls set "alls_msg" = "alls_msg" + 1""")
                cursor.execute(f"""UPDATE alls set "alls_chang" = "alls_chang" + {int(ttt)}""")
            # conn.commit()
    except KeyboardInterrupt as e:
        conn.commit()
        logg.warning(f"{namebd} = Cохранено")
        conn.close()
        logg.warning(f"{namebd} = Сойденение Закрыто")
        sys.exit(0)
