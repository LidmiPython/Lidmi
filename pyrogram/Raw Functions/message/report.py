@app.on_message()
async def report(_, msg):
    # Сообщить о жестоком обращении с детьми.
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonChildAbuse, 
    message="/"))

    # Отчет о защищенном авторским правом содержании.
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonCopyright, 
    message="/"))

    # Сообщить о выдаче себя за другое лицо. 
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonFake, 
    message="/"))

    # Сообщить о нерелевантной геогруппе.
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonGeoIrrelevant, 
    message="/"))

    # жалоба о наркотиках.
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonIllegalDrugs, 
    message="/"))

    # Другое
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonOther, 
    message="/"))

    # Заявление о разглашении личных данных.
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonPersonalDetails, 
    message="/"))

    # Сообщить о порнографии.
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonPornography, 
    message="/"))

    # Сообщить о насилии.
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonSpam, 
    message="/"))

    
    app.invoke(Report(peer=app.resolve_peer(msg.reply_to_message.from_user.id),
    id=app.resolve_peer(msg.reply_to_message_id),
    reason=InputReportReasonViolence, 
    message="/"))
