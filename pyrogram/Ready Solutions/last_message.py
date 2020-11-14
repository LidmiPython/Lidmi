from datetime import datetime, timedelta

@app.on_message(filters.me, group=-1)
async def last_message(client, message):
	await app.update_profile(bio=f"[{datetime.strftime(datetime.now(), '%H:%M:%S')}] ⇒ last message")
'''
Идея взята у t.me/CorneiZeR

'''
