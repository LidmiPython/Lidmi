@app.on_message(filters.command(["admins", "reports"], prefixes=command_prefix, case_sensitive=False))
async def report(_, msg):
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonChildAbuse, 
    message="/"))
