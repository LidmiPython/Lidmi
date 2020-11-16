from typing import Dict
import re
from time import time

from pyrogram import filters
from pyrogram.types import Message, ChatPermissions


@Client.on_message(filters.regex(r'^([Rr][Oo])|([Mm][Uu][Tt][Ee]) ((\d+|(\d+\.\d+))[mhdw])+$'))
def read_only(client: Client, message: Message):
    mute_seconds: int = 0
    for character in 'mhdw':
        match = re.search(rf'(\d+|(\d+\.\d+)){character}', message.text)    # Searching for a terms
        if match:   # calculating seconds if found valid term
            if character == 'm':
                mute_seconds += int(float(match.string[match.start():match.end() - 1]) * 60 // 1)
            if character == 'h':
                mute_seconds += int(float(match.string[match.start():match.end() - 1]) * 3600 // 1)
            if character == 'd':
                mute_seconds += int(float(match.string[match.start():match.end() - 1]) * 86400 // 1)
            if character == 'w':
                mute_seconds += int(float(match.string[match.start():match.end() - 1]) * 604800 // 1)
    if mute_seconds > 30:
        try:
            client.restrict_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id,
                ChatPermissions(),
                int(time()) + mute_seconds
            )
            from_user = message.reply_to_message.from_user
            mute_time: Dict[str, int] = {
                'days': mute_seconds // 86400,
                'hours': mute_seconds % 86400 // 3600,
                'minutes': mute_seconds % 86400 % 3600 // 60
            }
            message_text = f"<a href=\"tg://user?id={from_user.id}\">{from_user.first_name}" \
                           f"{from_user.last_name if from_user.last_name else ''}</a>" \
                           f" {('(@' + from_user.username + ')') if from_user.username else ''} was muted for" \
                           f" {((str(mute_time['days']) + ' day') if mute_time['days'] > 0 else '') + ('s' if mute_time['days'] > 1 else '')}" \
                           f" {((str(mute_time['hours']) + ' hour') if mute_time['hours'] > 0 else '') + ('s' if mute_time['hours'] > 1 else '')}" \
                           f" {((str(mute_time['minutes']) + ' minute') if mute_time['minutes'] > 0 else '') + ('s' if mute_time['minutes'] > 1 else '')}"
            while '  ' in message_text:
                message_text = message_text.replace('  ', ' ')
            message.edit_text(message_text)
        except Exception as e:
            print(e)
            return
