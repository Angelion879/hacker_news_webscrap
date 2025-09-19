"""module that builds and sends the message through ntfy app"""
import os
import requests

try:
    CHAN = os.environ["SECRET_CHANNEL"]
except KeyError:
    from keys import channel
    CHAN = channel

def create_text_message(news_list):
    '''builds the message string'''

    text_message = "\n\n".join(str("\n - ".join(str(j) for j in i)) for i in news_list)

    return text_message

def send_ntfy_message(message):
    '''sends the message through a post request on ntfy app'''
    requests.post(f"https://{CHAN}",
        data=f"{message}",
        headers={
            "Title": "Hacker News Update",
            "Tags": "computer",
        },
        timeout= 5)

if __name__ == '__main__':
    pass
