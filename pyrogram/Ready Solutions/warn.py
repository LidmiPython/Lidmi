import sqlite3
from time import time
from pyrogram.types import ChatPermissions

from pyrogram import filters

def message_text_filter(text):
    async def func(flt, _, msg):
        return flt.data == msg.text

    return filters.create(func, data=text)

@bot.on_message(message_text_filter("warn"))
def warning(client, message):
    user = bot.get_chat_member (message.chat.id, message.from_user.id)
    if user.status == "administrator" or user.status == "creator":
        namebd = f"basa_data/warn_base.db"
        conn = sqlite3.connect(namebd)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS warn ("id"	TEXT, "first_name" TEXT, "count" INTEGER)""")
        try:
            if message.reply_to_message:
                try:
                    user_id = message.reply_to_message.from_user.id
                    first_name = message.reply_to_message.from_user.first_name
                    start = cursor.execute("""SELECT count(id) FROM warn WHERE id=?""", (user_id,)).fetchone()
                    if user.can_restrict_members == True or user.status == "creator":
                        if start[0]==0:
                            cursor.execute("""INSERT INTO warn (id, first_name, count) VALUES(?,?,"1");""", (user_id, first_name,))
                            conn.commit()
                        else:
                            cursor.execute("""UPDATE warn set "count" = "count" + 1 WHERE id=?""", (user_id,))
                            conn.commit()
                        warn_count = cursor.execute("""SELECT count FROM warn WHERE id=?""", (user_id,)).fetchone()
                        if warn_count[0] <= 2:
                            bot.send_message(message.chat.id, f"[{first_name}](tg://user?id={user_id}) received a warning from Admin. {str(int(warn_count[0]-3))} warnings left")
                        if warn_count[0] == 3:
                            bot.restrict_chat_member (message.chat.id, message.reply_to_message.from_user.id, ChatPermissions(), int(time()) + 604800)
                            bot.send_message(message.chat.id, f"[{first_name}](tg://user?id={user_id}) Received mute for 7 days. for 3 warnings")
                        elif warn_count[0] == 4:
                            bot.restrict_chat_member (message.chat.id, message.reply_to_message.from_user.id, ChatPermissions (), int(time()) + 2419200)
                            bot.send_message (message.chat.id, f"[{first_name}](tg://user?id={user_id}) Received mute for 28 days. for 4 warnings")
                        elif warn_count[0] == 5:
                            bot.restrict_chat_member (message.chat.id, message.reply_to_message.from_user.id, ChatPermissions (), int(time()) + 9676800)
                            bot.send_message (message.chat.id, f"[{first_name}](tg://user?id={user_id}) Received mute for 112 days. for 5 warnings")
                        else:
                            bot.restrict_chat_member (message.chat.id, message.reply_to_message.from_user.id, ChatPermissions ()) # Мут на всегда
                            bot.send_message (message.chat.id, f"[{first_name}](tg://user?id={user_id}) Got mute on always. for 6 warnings")
                    else:
                        bot.send_message(message.chat.id, "Вы не имеете доступа к выдаче `warn`, из за отсуцтвия права на Блокировку")
                except:
                    cursor.execute("""UPDATE warn set "count" = "count" - 1 WHERE id=?""", (user_id,))
                    conn.commit()
            else:
                bot.send_message(message.chat.id, "чтоб выдать `warn`. Нужно ответить на сообщение")
        except:
            raise
    else:
        bot.send_message(message.chat.id, "Вы не имеете доступа к выдаче `warn`.")