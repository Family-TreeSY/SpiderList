# _*_ coding:utf-8 _*_

import requests
from lxml import etree

LOGIN_URL = 'https://github.com/login'
SESSION_URL = 'https://github.com/session'

s = requests.session()
y = s.get(LOGIN_URL)
tree = etree.HTML(y.text)
ele = tree.xpath('//input[@name="authenticity_token"]')[0]
authenticity_token = ele.attrib['value']

data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': 'fwuV3HbD15A9BKiEJVtsEYEqzDv+r+yG9rj0uuFKLPtKjeK00ubWkbmKqQ6VJp9worJ5BVGMz3ZJV9Feyg9IKw==',
    'login': '用户名',
    'password': '1234567'
}

y = s.post(SESSION_URL, data=data)
print y.url


