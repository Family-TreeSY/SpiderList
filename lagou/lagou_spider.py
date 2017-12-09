# -*- coding:utf-8 -*-

import requests
import time
import random
import datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.lagou
job = db.job

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
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '25',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'user_trace_token=20170919133428-34842e32-9cfc-11e7-919b-5254005c3644;'
              ' LGUID=20170919133428-34843393-9cfc-11e7-919b-5254005c3644;'
              ' index_location_city=%E5%85%A8%E5%9B%BD;'
              ' _gid=GA1.2.489551564.1512647723;'
              ' _ga=GA1.2.399924787.1505799456;'
              ' Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512647723,1512699432,1512710468,1512785411;'
              ' Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512788669;'
              ' LGRID=20171209110429-ac07e127-dc8d-11e7-9c96-5254005c3644;'
              ' TG-TRACK-CODE=search_code;'
              ' JSESSIONID=ABAAABAAAIAACBIE33A4ECAC65A4DB3CF468D3BDC87D59C;'
              ' SEARCH_ID=6899d4adad624db4bbe6cb768482fad6',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&city=%E4%B8%8A%E6%B5%B7',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': random.choice(user_agents)
}

def get_data(url):
    for i in range(1, 17):
        data = {
            'first': 'true',
            'pn': i,
            'kd': 'Python'
        }

        json = requests.post(url, data=data, headers=headers).json()
        positions = json['content']['positionResult']['result']

        #job_list = []

        for position in positions:
            datas = [{
                'positionName': position['positionName'],
                'workYear': position['workYear'],
                'education': position['education'],
                'jobNature': position['jobNature'],
                'companyShortName': position['companyShortName'],
                'district': position['district'],
                'createTime': position['createTime'],
                'businessZones': position['businessZones'],
                'datetime': datetime.datetime.now()
            }]

            #job_list.append(datas)
            mogo = job.insert_many(datas)
            #time.sleep(7)
            print(mogo)
        #return job_list


def main():
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false&isSchoolJob=0'
    job_info = get_data(url)

    time.sleep(10)
    print(job_info)

if __name__ == "__main__":
    main()