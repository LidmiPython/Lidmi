#class pyrogram.types.ChatPreview
#https://docs.pyrogram.org/api/types/ChatPreview#pyrogram.types.ChatPreview

message.chat_preview.title         # ( str) - Заголовок чата.
message.chat_preview.type          # ( str) - Тип чата, может быть «группа», «супергруппа» или «канал».
message.chat_preview.members_count # ( int) - Количество участников чата.
message.chat_preview.photo         # ( Photo, необязательно ) - фото чата.
message.chat_preview.members       # ( List of User, необязательно ) - Предварительный просмотр некоторых участников чата.
