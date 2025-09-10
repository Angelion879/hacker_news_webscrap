import requests
from bs4 import BeautifulSoup as bs

def create_list_of_titles_and_links(soup_obj):
    title_content = soup_obj.select('.titleline')
    titles = []

    for i,item in enumerate(title_content):
        text_title = item.get_text()
        href_link = item.select('a')[0].get('href', None)
        titles.append([text_title, href_link])

    return titles

def create_list_of_votes(soup_obj):
    vote_content = soup_obj.select('.score')
    votes = []

    for i,item in enumerate(vote_content):
        vote_count = item.get_text().split(' ')[0]
        votes.append(vote_count)

    return votes

def create_relevant_news_list(soup_obj):
    vote_list = create_list_of_votes(soup_obj)
    news_list = create_list_of_titles_and_links(soup_obj)
    news = []

    for i, item in enumerate(vote_list):
        if int(item) >= 200:
            news.append(news_list[i])

    return news

def create_text_message(soup_obj):
    news_list = create_relevant_news_list(soup_obj)
    text_message = "\n\n".join(str("\n - ".join(str(j) for j in i)) for i in news_list)

    return text_message


if __name__ == '__main__':
    res = requests.get('https://news.ycombinator.com/news')
    soup = bs(res.text, 'html.parser')

    txt = create_text_message(soup)

    print(txt)
