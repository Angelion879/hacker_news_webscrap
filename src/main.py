"""main file for the hacker news web-scrapper"""
import requests
from bs4 import BeautifulSoup as bs
import scrap as s
import messager as m

def connection():
    '''gets the html page and handles the possible connection error'''
    try:
        site = requests.get('https://news.ycombinator.com/news', timeout=5)
    except TimeoutError:
        connection()

    return site

if __name__ == '__main__':
    web_pg = connection()
    HTML_SOUP = bs(web_pg.text, 'html.parser')

    news_list = s.create_relevant_news_list(HTML_SOUP)
    MESSAGE = m.create_text_message(news_list)

    m.send_ntfy_message(MESSAGE)
