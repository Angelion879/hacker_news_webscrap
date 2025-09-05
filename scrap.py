import requests
from bs4 import BeautifulSoup as bs
import subprocess
from keys import channel

res = requests.get('https://news.ycombinator.com/news')
soup = bs(res.text, 'html.parser')

# print(soup.select('.titleline')[0].get_text())
# print(soup.select('.titleline')[0].select('a')[0].get('href'))
# print(soup.select('.score')[0].get_text())

# BzYUG0zECQ43N6A9

titles = soup.select('.titleline')
votes = soup.select('.score')

def news_cleanup(t_list, v_list):
    news = []
    try:
        for i in range(50):

            s = v_list[i].get_text().split(' ')
            n = t_list[i].get_text()
            l = t_list[i].select('a')[0].get('href', None)

            if int(s[0]) >= 200:
                news.append([n,l])
    except IndexError:
        print("Done!")

    return news

news_list = news_cleanup(titles, votes)

text_message = "\n\n".join(str("\n - ".join(str(j) for j in i)) for i in news_list)

sender = subprocess.run(f'curl -d "{text_message}" {channel}')
