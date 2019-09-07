import random

import requests
from bs4 import BeautifulSoup


# house rabbit society not whitelisted by pythonanywhere
def hrs_get_src():
    page = requests.get('https://rabbit.org/fun/net-bunnies.html')
    if page.status_code != 200:
        return None

    return BeautifulSoup(
        page.content, 'html.parser'
        ).select_one('a[href="net-bunnies.html"] + br + img')['src']
    

def pix_get_src():
    r = random.randint(1, 5)

    page = requests.get(f'https://pixabay.com/photos/search/rabbit/?cat=animals&pagi={r}')
    if page.status_code != 200:
        return None

    items = BeautifulSoup(page.content, 'html.parser').select('div.item')
    photos = [
        item.select_one('a') for item in items
        if "Rabbit" in ' '.join(i.text for i in item.select('span > a'))
        or "Hare" in ' '.join(i.text for i in item.select('span > a'))
        and "Easter" not in ' '.join(i.text for i in item.select('span > a'))
    ]
    
    link = f"https://pixabay.com{photos[random.randint(0, len(photos) - 1)]['href']}"

    print(link)

    inner_page = requests.get(link)
    if inner_page.status_code != 200:
        return None

    return BeautifulSoup(
        inner_page.content, 'html.parser'
        ).select_one('div#media_container img')['src']

if __name__ == "__main__":
    pix_get_src()
