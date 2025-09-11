"""main file for the hacker news web-scrapper"""
import os
import requests
from bs4 import BeautifulSoup as bs
import scrap as s

def send_ntfy_message(message):
    requests.post(f"https://{CHAN}",
        data=f"{message}",
        headers={
            "Title": "Hacker News Update",
            "Tags": "computer",
        })


if __name__ == '__main__':
    site = requests.get('https://news.ycombinator.com/news')
    HTML_SOUP = bs(site.text, 'html.parser')

    try:
        CHAN = os.environ["SECRET_CHANNEL"]
    except KeyError:
        from keys import channel
        CHAN = channel

    news_message = s.create_text_message(HTML_SOUP)

    send_ntfy_message(news_message)
