import requests

url = "https://api.telegram.org/bot575720932: AAHoVwfr_CdPOG1919kI27t4KHMAtpXq_-g/"


def get_bot_updates(limit, offset):
    url = "https://api.telegram.org/bot575720932:AAHoVwfr_CdPOG1919kI27t4KHMAtpXq_-g/getUpdates"
    params = {'limit': limit, 'offset': offset}
    result = requests.get(url, params=params)
    decoded = result.json()
    return decoded['result']


def send_message(chat_id, text):
    url = "https://api.telegram.org/bot575720932:AAHoVwfr_CdPOG1919kI27t4KHMAtpXq_-g/sendMessage"
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, 'test', params=params)
    return response


result = get_bot_updates(5, 0)
for update in result:
    Update_message = update['message']
    chat_id = update['message']['chat']['id']
    last_message = update['update_id']
    send_message(chat_id, 'test')
