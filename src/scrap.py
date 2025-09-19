"""this module contains the web-scrapping functions for the hacker news website"""

def create_list_of_titles_and_links(soup_obj):
    '''creates a list with the titles of the news and the links to the related pages'''
    title_content = soup_obj.select('.titleline')
    titles = []

    for i,item in enumerate(title_content):
        text_title = item.get_text().replace('\n','').replace('\t','')
        href_link = item.select('a')[0].get('href', None)
        titles.append([text_title, href_link])

    return titles

def create_list_of_votes(soup_obj):
    '''creates a list with the votes/scores of each topic'''
    vote_content = soup_obj.select('.score')
    votes = []

    for i,item in enumerate(vote_content):
        vote_count = item.get_text().split(' ')[0]
        votes.append(vote_count)

    return votes

def create_relevant_news_list(soup_obj):
    '''builds a list with only the relevant news, the ones with a score of, at least, 200'''
    vote_list = create_list_of_votes(soup_obj)
    news_list = create_list_of_titles_and_links(soup_obj)
    news = []

    for i, item in enumerate(vote_list):
        if int(item) >= 200:
            news.append(news_list[i])

    return news

if __name__ == '__main__':
    pass
