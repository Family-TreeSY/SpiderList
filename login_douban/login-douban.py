# _*_ coding=utf-8 _*_
__author__ = 'Treehl'

'''
模拟登陆豆瓣
'''
import requests
from bs4 import BeautifulSoup
from http import cookiejar

download_url = 'https://accounts.douban.com/login'
captcha_url = 'https://www.douban.com/misc/captcha?id=umLh3z1YQonVGyANZOAm6hfG:en&size=s'
data = {
    'source': 'index_nav',
    'redir': 'https://accounts.douban.com/session',
    'captcha-solution': 'dsasdada',
    'captcha-id': 'AA69lJ49jAuUSFQScH4zfFbeA:en',
    'login': '登录'
}

headers = {
    'Host': 'accounts.douban.com',
    'Referer': 'https://accounts.douban.com/login?alias=286210002%40qq.com&redir=https%3A%2F%2Faccounts.douban.com%2Fsession&source=index_nav&error=1016',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='cookies')
try:
    print(session.cookies)
    session.cookies.load(ignore_discard=True)
except:
    print('no cookie')
    print(input('Please input your email: '))
    print(input('Please input your password：'))

def get_captcha():
    '''
    把验证码图片保存到当前目录，手动识别验证码
    :return:
    '''
    r = requests.post(download_url, data=data, headers=headers)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')
    image = soup.find('img', attrs={'id': 'captcha_image'}).get('src')
    s = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(s.content)
    captcha = input('Please input the captcha: ')
    captcha_id = soup.find('input', {'type': 'hidden', 'name': 'captcha-id' }).get('value')
    return captcha, captcha_id

def login():
    captcha, captcha_id = get_captcha()
    # 增加表数据
    data['captcha-solution'] = captcha
    data['captcha-id'] = captcha_id
    response = session.post(download_url, data=data, headers=headers)
    page = response.text
    print(page)
    session.cookies.save()

if __name__ == '__main__':
    login()