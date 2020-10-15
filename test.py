

import requests
import json
# url_send_message = """https://api.telegram.org/bot544273446:AAF57lolMySZtDSP-EE5fiBh0tq4fKLDWDg/sendMessage"""
# headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
# message = {
#     "chat_id": 81432612,
#     "text": "Внимание, открыт аккаунт - {}".format(user)
# }
# payload = json.dumps(message)
# r = requests.get(url_send_message, data=payload, headers=headers)
# r = requests.get(url_send_message)

payload = {
    "update_id": 243475549,
    "message": {
        "message_id": 9450,
        "from": {
            "id": 81432612,
            "is_bot": False,
            "first_name": "Kirill",
            "username": "kkkkk_kkk_kkkkk",
            "language_code": "ru"
        },
        "chat": {
            "id": 81432612,
            "first_name": "Kirill",
            "username": "kkkkk_kkk_kkkkk",
            "type": "private"
        },
        "date": 1589404439,
        "text": "привет"
    }
}
#
# print(payload.keys())
#
# print(payload['message']['from']['id'])
#
# print(payload['message']['text'])

d = {}

d[0] = 0

print(d)
from time import sleep
for i in range(10):
    print(i)
    sleep(1)

