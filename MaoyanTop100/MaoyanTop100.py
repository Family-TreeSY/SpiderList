# -*- coding:utf-8 -*-
import json

import requests
import random
from bs4 import BeautifulSoup
from multiprocessing import Pool
from requests.exceptions import RequestException
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.MaoyanTop250
maoyan = db.maoyan


user_agents = [
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2995.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2986.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.0 Safari/537.36'
]


headers ={
    'Host':'maoyan.com',
    'Referer':'http://maoyan.com/board/4?offset=90',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':random.choice(user_agents)
}


def get_page(url):
    # try:
    #     response = requests.get(url,headers=headers)
    #     if response.status_code == 200:
    #         return response.text
    #     return None
    # except RequestException:
    #     return None
    return requests.get(url, headers=headers).content


def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    # tree = etree.HTML(html)
    # movie_name = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[1]/a/text()')
    # movie_actor = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[2]/text()')
    # movie_published = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[3]/text()')
    # movie_star = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[2]/p/i[1]/text()')
    movie_lists = soup.find('dl', {'class': 'board-wrapper'})
    # print(movie_list)
    movies = []
    for movie_list in movie_lists.find_all('dd'):
        movie_name = movie_list.find('p', {'class': 'name'}).get_text()
        movie_actor = movie_list.find('p', {'class': 'star'}).get_text()
        movie_published = movie_list.find('p', {'class': 'releasetime'}).get_text()
        movie_star = movie_list.find('i', {'class': 'integer'}).get_text()
        data = {
            'name': movie_name,
            'actor': movie_actor,
            'published': movie_published,
            'star': movie_star
        }

        movies.append(data)
    return movies


def save_to_mongodb(data):
    try:
        if maoyan.insert(data):
            print('Save to mongodb succesfully!')
    except:
        print('Save Error!')
    finally:
        print(data)


def write_to_file(data):
    try:
        with open('maoyan.text', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
    except:
        print('Write Error!')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_page(url)
    data = parse_page(html)
    save_to_mongodb(data)
    write_to_file(data)



if __name__ == '__main__':
    # main()
    p = Pool(8)
    p.map(main, [i*10 for i in range(10)])
    # for i in range(10):
    #     main(i*10)
    p.close()
    p.join()
    print('All Done!')