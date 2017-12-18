# -*- coding:utf-8 -*-

import datetime
import json
import requests
from multiprocessing import Pool
from urllib.parse import urlencode
from pymongo import MongoClient
from requests.exceptions import RequestException
from  config import *

client = MongoClient('localhost', 27017)
db = client.toutiao
news = db.news


def get_data(offset):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': '江歌',
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from':'search_tab'
    }

    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('data is error!')
        return None

def parse_data(html):
    data = json.loads(html) # JSON 字符串解码为 Python 对象
    if data and 'data' in data.keys():
        news_list =[]
        for item in data.get('data'):
            news = {
                'title': item.get('title'), # 使用get()方法避免了部分keys不存在时报错
                'url': item.get('url'),
                'datetime': datetime.datetime.now()
            }
            news_list.append(news)
        return news_list

def save_to_mongo(data):
    try:
        if news.insert(data):
            print('Save succesfully!')
    except:
        print('Save Error!')
    finally:
        print(data)

def main(offset):
    html = get_data(offset)
    data = parse_data(html)
    datebase = save_to_mongo(data)
    print(datebase)


if __name__ == '__main__':
    # main()
    groups = [x * 2 for x in range(GROUP_START, GROUP_END + 1)]
    pool = Pool(8)
    pool.map(main, groups)
    pool.close()
    pool.join()
    print('ALl is done!')






