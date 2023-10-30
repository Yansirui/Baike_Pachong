# coding=utf-8
from bs4 import BeautifulSoup
import os
from urllib.parse import unquote
dir=os.listdir('html_v2')

all_items_url=[]
j=1
with open('item扩展_v4.txt','w',encoding='utf-8') as f:
    for file in dir:
        soup = BeautifulSoup(open(r'html_v2/'+file,'r',encoding='utf-8'),"html.parser")
        # 现在 `soup` 包含了解析后的内容
        for link in soup.find_all('a'):
            url = link.get('href')
            if url == None:
                continue
            else:
                if 'http' in url:
                    continue
                else:
                    url = unquote(url)
                    #有些所有页面都有的item需要去除
                    if ('item' in url) and ('百科' not in url) and ('viewPageContent' not in url)  and ('秒懂' not in url):
                        if 'https://baike.baidu.com'+url not in all_items_url:
                            all_items_url.append('https://baike.baidu.com'+url)
            if len(all_items_url) % 500==0:
                for item in all_items_url:
                    f.write(item + '\n')
                all_items_url=[]
                print('Save_tems_nums:{}'.format(j*500))
                j=j+1
    if len(all_items_url) > 0:
        for item in all_items_url:
            f.write(item + '\n')
print(len(all_items_url))
