import requests
from bs4 import BeautifulSoup
from time import sleep
import random

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}


def get_info_main_page():

    url = 'https://mcpehub.org/maps/'

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.find_all('article', class_="col-xs-12 col-sm-4 col-md-6")

    return_data_list = []

    for article in data:
        map_url = article.find('a', class_="news-item border-radius").get('href')
        map_title = article.find('h2', class_="black medium").text
        map_img = 'https://mcpehub.org' + article.find('div', class_="news-image").find('img').get('src')
        map_desc = article.find('p', class_="black regular").text

        info = ({'map_title': map_title, 'map_description': map_desc, 'map_url': map_url, 'map_img': map_img})
        # print(f"{info}")

        return_data_list.append(info)

    return return_data_list


def get_urls(i, for_all=False):
    main_pg_data = get_info_main_page()
    count = 0

    if for_all:
        for el in range(0, i+1):
            url = main_pg_data[count]['map_url']

            print(url)

            count += 1

    if not for_all:
        url = main_pg_data[i]['map_url']
        print(url)


get_urls(9, for_all=False)

# Status: working...
