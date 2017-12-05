# -*- coding:utf-8 -*-

import requests
import time
import random
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 连接数据库
client = MongoClient('localhost', 27017)
# 创建数据库
db = client.lianjia
# 创建集合
homes = db.homes


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

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'sh.lianjia.com',
    'Referer': 'http://sh.lianjia.com/ershoufang',
    'Upgrade-Insecure-Requests': '1',
    'User_Agent': random.choice(user_agents)
}

#url = 'http://sh.lianjia.com/ershoufang/baoshan'
def get_rooms():
    for i in range(81, 101):
        #time.sleep(2)
        r = requests.get('http://sh.lianjia.com/ershoufang/baoshan/d' + str(i), headers=headers)
        print(r.url)
        #print(r.status_code)
        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup.prettify())
        rooms = soup.find('ul', attrs={'class': 'js_fang_list'})


        for room in rooms.find_all('li'):
            room_title = room.find('div', attrs={'class': 'prop-title'}).get_text()
            room_info = room.find('span', attrs={'class': 'info-col row1-text'}).get_text()
            room_location = room.find('span', attrs={'class': 'info-col row2-text'}).find('a').get_text()
            room_price = room.find('span', attrs={'class': 'total-price strong-num'}).get_text()
            room_unit_price = room.find('span', attrs={'class': 'info-col price-item minor'}).get_text()
            extra_info = room.find('div', attrs={'class': 'property-tag-container'}).get_text()
            #time.sleep(5)
            #print(room_title, room_info, room_location,room_price, room_unit_price, extra_info)

            rooms_list = []

            rooms_info ={
                'title': room_title,
                'info': room_info,
                'location': room_location,
                'price': room_price,
                'unit_proce': room_unit_price,
                'message': extra_info,
                'time': datetime.datetime.now()
            }

            rooms_list.append(rooms_info)
            #print(rooms_list)
            result = homes.insert_many(rooms_list)
            time.sleep(2)
            print(result)


def main():
    rooms = get_rooms()
    time.sleep(2)
    print(rooms)

if __name__ == "__main__":
    main()