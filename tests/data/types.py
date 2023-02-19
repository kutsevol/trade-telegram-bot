USER = {
    "id": 12345678,
    "is_bot": False,
    "first_name": "FirstName",
    "last_name": "LastName",
    "username": "username",
    "language_code": "en",
}

CHAT = {
    "id": 12345678,
    "first_name": "FirstName",
    "last_name": "LastName",
    "username": "username",
    "type": "private",
}

MESSAGE = {
    "message_id": 11223,
    "from": USER,
    "chat": CHAT,
    "date": 1508709711,
    "text": "Hi, world!",
}

DOCUMENT = {
    "file_name": "data.csv",
    "mime_type": "text/csv",
    "file_id": "BQACAgIAAxkBAAIp72PkFldoQJRkoVsslOBDcwOghmW1AAK0LAACG24hS7SAvCoGbdpoLgQ",
    "file_unique_id": "AgADtCwAAhtuIUs",
    "file_size": 25206,
}

MESSAGE_WITH_DOCUMENT = {
    "message_id": 12345,
    "from": USER,
    "chat": CHAT,
    "date": 1508768012,
    "document": DOCUMENT,
    "caption": "Read my document",
}
