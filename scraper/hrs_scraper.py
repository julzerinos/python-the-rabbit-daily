import requests

from bs4 import BeautifulSoup


def get_rabbit_link():
    page = requests.get('https://rabbit.org/fun/net-bunnies.html')
    if page.status_code != 200:
        return None

    return BeautifulSoup(
        page.content, 'html.parser'
        ).select_one('a[href="net-bunnies.html"] + br + img')['src']
    