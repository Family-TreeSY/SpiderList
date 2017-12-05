# _*_ coding=utf-8 _*_
__author__ = 'Treehl'
'''
爬取豆瓣小说
'''
import requests
import codecs
from bs4 import BeautifulSoup

download_url = 'https://read.douban.com/kind/100'

def download_page(url):
    return requests.get(url, headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    read_list_soup = soup.find('ul', attrs={'class': 'list-lined ebook-list column-list'})

    read_name_list = []

    for read_li in read_list_soup.find_all('li', attrs={'class': 'item store-item'}):
        detail = read_li.find('div', attrs={'class': 'title'})
        read_name = detail.find('a').getText()
        read_name_list.append(read_name)

    next_page = soup.find('li', attrs={'class': 'next'}).find('a')
    if next_page:
        return read_name_list, download_url + next_page['href']
    return read_name_list, None


def main():
    url = download_url

    with codecs.open('readings', 'wb', encoding='utf-8') as f:
        while url:
            html = download_page(url)
            readings, url = parse_html(html)
            f.write(u'{readings}\n'.format(readings='\n'.join(readings)))


if __name__ == '__main__':
    main()