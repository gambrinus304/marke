import requests
from settings import token

url = "https://api.telegram.org/bot575720932:"


def get_bot_updates(limit, offset):
    link = (url + token + 'getUpdates')
    params = {'limit': limit, 'offset': offset}
    result = requests.get(link, params=params)
    decoded = result.json()
    return decoded['result']


def send_message(chat_id, text):
    link = (url + token + 'sendMessage')
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(link, 'test', params=params)
    return response


def bot_commands(new_update):
    for update in new_update:
        update_message = update['message']
        chat_id = update['message']['chat']['id']
        input_message = update['message']['text']
        last_message = update['update_id']
        if input_message:
            send_message(chat_id, 'test')


# while True: - пока так, иначе будет бесконечно спамить

new_update = get_bot_updates(5, 0)
bot_commands(new_update)


# на данный момент это все, что получилось, к сожалению. Бот при запуске почему-то отсылает 5 сообщений - независимо от того, есть сообщения от пользователя или нет.
