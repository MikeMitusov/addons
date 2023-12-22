import requests
from bs4 import BeautifulSoup
from time import sleep
import random

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}


def get_info(from_p=0, to_pgs=1):
    for num in range(from_p, to_pgs):
        sleep(random.choice([3.1, 3.2, 3.4, 4.1, 3.8, 4.5]))
        url = f'https://mcpehub.org/mods/page/{num}/'

        response = requests.get(url, headers=headers)

        soup_1 = BeautifulSoup(response.text, 'lxml')

        mod_card = soup_1.find_all('article', class_="col-xs-12 col-sm-4 col-md-6")

        for mod in mod_card:
            files = []
            mod_name = mod.find('h2', class_="black medium").text
            mod_desc = mod.find('p', class_="black regular").text
            mod_url = mod.find('a', class_="news-item border-radius").get('href')

            response_mod = requests.get(mod_url, headers=headers)
            soup_2 = BeautifulSoup(response_mod.text, 'lxml')

            download_url = soup_2.find_all('a', class_='flex middle center green-bg medium white')
            for url_file in download_url:
                url_file = url_file.get('href')
                files.append(url_file)

            mod_img = 'https://mcpehub.org' + mod.find('div', class_='news-image').find('img').get('src')
            final_print = f"{mod_name}\n{mod_desc}\nMore: {mod_url}\nImage: {mod_img}\nFiles: {files}\n"
            print(final_print)

            with open('mods.txt', 'a', encoding='utf-8') as text:
                text.write(f'{mod_name}\n')
                text.write(f'{mod_desc}\n')
                text.write(f"More: {mod_url}\n")
                text.write(f"Image: {mod_img}\n")
                text.write(f"Files: {files}\n")
                text.write('\n')


if __name__ == '__main__':
    from_page = int(input('From page: '))
    to_pages = int(input('To page: '))
    print(get_info(from_page, to_pages))