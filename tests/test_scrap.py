"""this is a test file for the web-scrapper functions"""
import sys
import unittest
from bs4 import BeautifulSoup as bs

sys.path.append('../')
from src import scrap

class TestHackerNewsScrapper(unittest.TestCase):
    """Tests regarding the scrap.py functions"""

    with open('page_mock.html') as test_html:
        soap = bs(test_html, 'html.parser')

    def test_title_and_link_list_creation(self):
        test_title_list = scrap.create_list_of_titles_and_links(self.soap)
        expected = [['This is a test title', 'https://example.com'],
                    ['Another test title', 'https://example2.com'],
                    ['Guess what? Test titles!', 'https://example3.com']]

        self.assertEqual(test_title_list, expected)

    def test_vote_list_creation(self):
        test_title_list = scrap.create_list_of_votes(self.soap)
        expected = ['244',
                    '120',
                    '301']

        self.assertEqual(test_title_list, expected)
