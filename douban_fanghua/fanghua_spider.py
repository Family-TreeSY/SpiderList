# -*- coding:utf-8 -*-

import json
import random

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from pymongo import MongoClient
from multiprocessing import Pool


client = MongoClient('localhost', 27017)
db = client.fanghua
fh = db.fh


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
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'bid=CG9JBGv2HTc; ll="118172"; __yadk_uid=C8aGLFZrayraTbqegT74s17VApyvgZLj; gr_user_id=921f5343-544d-480f-b1a5-8f014ef16eb7; _ga=GA1.2.1699865973.1505868305; ps=y; ue="286210002@qq.com"; push_noty_num=0; push_doumail_num=0; viewed="25862578_26698660_1200840_1003000_27064644_26878124_27006492_1008145_27045888_25967870"; ap=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1513821890%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E8%258A%25B3%25E5%258D%258E%22%5D; _vwo_uuid_v2=16662DD85FE53735E33BEE7823CD8403|e6899e043dee26f7fb0a73189255bec2; __utmt=1; __utma=30149280.1699865973.1505868305.1513750738.1513821890.63; __utmb=30149280.1.10.1513821890; __utmc=30149280; __utmz=30149280.1513821890.63.35.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmv=30149280.16701; __utma=223695111.1400870841.1505868305.1513750738.1513821890.51; __utmb=223695111.0.10.1513821890; __utmc=223695111; __utmz=223695111.1513821890.51.30.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; _pk_id.100001.4cf6=468c432b1127ff5d.1505868305.50.1513821901.1513750747.; _pk_ses.100001.4cf6=*',
    'Host':'movie.douban.com',
    'Referer':'https://movie.douban.com/subject/26862829/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': random.choice(user_agents)
}

def get_data(url):
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    comments= soup.find('div', attrs={'class': 'article'})
    comment_list = []
    for comment in comments.find_all('div', attrs={'class': 'main review-item'}):
        user_name = comment.find('header', attrs={'class': 'main-hd'}).find('a', attrs={'class': 'name'}).get_text()
        comment_time = comment.find('header', attrs={'class': 'main-hd'}).find('span', attrs={'class': 'main-meta'}).get_text()
        profile_picture = comment.find('header', attrs={'class': 'main-hd'}).find('img')['src']
        title = comment.find('h2').find('a').get_text()
        comment_info = comment.find('div', {'class': 'short-content'}).get_text()
        comment_detail = comment.find('h2').find('a')['href']
        like = comment.find('div', {'class': 'action'}).find('a', {'class': 'action-btn up'}).get_text()
        dislike = comment.find('div', {'class': 'action'}).find('a', {'class': 'action-btn down'}).get_text()
        respond = comment.find('div', {'class': 'action'}).find('a', {'class': 'reply'}).get_text()
        # print(user_name)
        # print(comment_time)
        # print(profile_picture)
        # print(title)
        # print(comment_info)
        # print(comment_detail)
        # print(like)
        # print(dislike)
        # print(respond)
        data = {
            'user_name': user_name,
            'comment_time': comment_time,
            'profile_picture': profile_picture,
            'title': title,
            'comment_info': comment_info,
            'comment_detail': comment_detail,
            'like': like,
            'dislike': dislike,
            'resond': respond
        }

        comment_list.append(data)
    return comment_list

def write_to_file(data):
    try:
        with open('fanghua.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
    except:
        print('Write Error!')


def save_to_mongo(data):
    try:
        if fh.insert(data):
            print('Save to mongodb Successfully!')
    except:
        print('Save Error!')
    finally:
        print(data)

def main(i):
    url = 'https://movie.douban.com/subject/26862829/reviews?start=' + str(i)
    html = get_data(url)
    data = parse_data(html)
    file = write_to_file(data)
    database = save_to_mongo(data)
    print(database, file)

if __name__ == '__main__':
    p = Pool(8)
    p.map(main, [i*20 for i in range(252)])
    p.close()
    p.join()
    print('ALL done!')
    # for i in range(252):
    #     main(i * 20)
