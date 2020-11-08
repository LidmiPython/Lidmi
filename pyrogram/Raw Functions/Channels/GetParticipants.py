from pyrogram.raw.functions.channels import GetParticipants #Получить участников канала
from pyrogram.raw.types import channelParticipantsRecent     #Получить только недавних участников
from pyrogram.raw.types import channelParticipantsAdmins     #Получить только участников с правами администратора
from pyrogram.raw.types import channelParticipantsKicked     #Получить только удаленных участников (Черный Список)
from pyrogram.raw.types import channelParticipantsBots       #Получить только участников-ботов
from pyrogram.raw.types import channelParticipantsBanned     #Получить только забаненных участников (исключения)
from pyrogram.raw.types import channelParticipantsSearch     #Поиск участников по имени
from pyrogram.raw.types import channelParticipantsContacts   #Поиск только участников, которые также являются контактами

#Получить только недавних участников
@app.on_message()
async def channels_GetParticipants_ChannelParticipantsRecent(client, message):
	msg = await app.send(GetParticipants(
		channel=await app.resolve_peer(-1001158541073),
		filter=ChannelParticipantsRecent(),
		offset=0,
		limit=0,
		hash=0))
	print(msg)

#Получить только участников с правами администратора
@app.on_message()
async def channels_GetParticipant_ChannelParticipantsAdmins(client, message):
	msg = await app.send(GetParticipants(
		channel=await app.resolve_peer(-1001158541073),
		filter=ChannelParticipantsAdmins(),
		offset=0,
		limit=0,
		hash=0))
	print(msg)

#Получить только удаленных участников (Черный Список)
@app.on_message()
async def channels_GetParticipants_ChannelParticipantsKicked(client, message):
	msg = await app.send(GetParticipants(
		channel=await app.resolve_peer(-1001158541073),
		filter=ChannelParticipantsKicked(q=""),
		offset=0,
		limit=0,
		hash=0))
	print(msg)

#Получить только участников-ботов
@app.on_message()
async def channels_GetParticipants_ChannelParticipantsBots(client, message):
	msg = await app.send(GetParticipants(
		channel=await app.resolve_peer(-1001158541073),
		filter=ChannelParticipantsBots(),
		offset=0,
		limit=0,
		hash=0))
	print(msg)


#Получить только забаненных участников (исключения)
@app.on_message()
async def channels_GetParticipants_ChannelParticipantsBanned(client, message):
	msg = await app.send(GetParticipants(
		channel=await app.resolve_peer(-1001158541073),
		filter=ChannelParticipantsBanned(q=""),
		offset=0,
		limit=0,
		hash=0))
	print(msg)

#поиск участников по имени
@app.on_message()
async def channels_GetParticipants_channelParticipantsSearch(client, message):
	msg = await app.send(GetParticipants(
		channel=await app.resolve_peer(-1001158541073),
		filter=ChannelParticipantsSearch(q=""),
		offset=0,
		limit=0,
		hash=0))
	print(msg)

#Выбирать только участников, которые также являются контактами
@app.on_message()
async def channels_GetParticipants_ChannelParticipantsContacts(client, message):
	msg = await app.send(GetParticipants(
		channel=await app.resolve_peer(-1001158541073),
		filter=ChannelParticipantsContacts(q=""),
		offset=0,
		limit=0,
		hash=0))
	print(msg)
