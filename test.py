import requests

print(requests.post('http://127.0.0.1:5000/post', json={
    "meta": {
        "locale": "ru-RU",
        "timezone": "UTC",
        "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
        "interfaces": {
            "screen": {},
            "payments": {},
            "account_linking": {}
        }
    },
    "session": {
        "message_id": 0,
        "session_id": "d3ee77a5-dd6a-4317-a2cc-1a398b0b3596",
        "skill_id": "0c0f784c-3852-4d4e-89ea-c95114bda70b",
        "user": {
            "user_id": "74C1B7EA67A9637933D03F3527A4B840C530FFB7DCDCEF288FB49CD020EC9563"
        },
        "application": {
            "application_id": "B5E1588EF5A873989DAEDC2BC9F011FC1DF34EB62B02762AB005B9DA5AC918F6"
        },
        "new": True,
        "user_id": "B5E1588EF5A873989DAEDC2BC9F011FC1DF34EB62B02762AB005B9DA5AC918F6"
    },
    "request": {
        "command": "",
        "original_utterance": "",
        "nlu": {
            "tokens": [],
            "entities": [],
            "intents": {}
        },
        "markup": {
            "dangerous_context": False
        },
        "type": "SimpleUtterance"
    },
    "version": "1.0"
}).json())
