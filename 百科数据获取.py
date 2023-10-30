from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import json
import re
# coding=utf-8
import urllib
from urllib import parse
def read_json(json_path):
    with open(json_path,'r',encoding='utf-8') as f:
        str=f.read()
        data=json.loads(str)
        return data
#html_v1获取网页内容
'''
terms=read_json(r'terms_v1.json')[1525:]
browser = webdriver.Edge(r"D:\Microsoft\msedgedriver.exe")
browser.get('https://baike.baidu.com/')
action_chains = ActionChains(browser)
for term in terms:
    print(term)
    for i in range(5):
        try:
            search_box=browser.find_element('id','query')
            search_box.clear()
            search_box.send_keys(term['term'])
            time.sleep(1)
            search_button=browser.find_element('id','search')
            action_chains.click(search_button).perform()
            url=browser.current_url
            request = requests.get(url)
            txt=request.text
            if 'summary' not in txt:
                pattern=r'"/item/'+term['term']+r'.*?"'
                txt = urllib.parse.unquote(txt)
                if '未收录' in txt:
                    break
                all_url=re.findall(pattern,txt)
                url='https://baike.baidu.com'+all_url[0].replace(r'"','')
            content=requests.get(url).text
            t=term['term'].replace('/','')
            with open(r'html_v1/baike_'+t+'.txt','w',encoding='utf-8') as f:
                f.write(content)
            time.sleep(1)
            break
        except NoSuchElementException:
            browser.refresh()
    else:
        continue

browser.quit()
'''

#html_v2网页内容获取

with open('item扩展_v3.txt','r',encoding='utf-8') as f:
    urls = f.readlines()

for url in urls:
    url = url.replace('\n','')
    t = url.split('/')[4]
    print('url:{0} , term:{1}'.format(url,t))
    content = requests.get(url).text
    times=0
    while '百度百科-验证' in content:
        if times == 10:
            break
        content = requests.get(url).text
        times = times+1
    if '百度百科-验证' in content:
        continue
    with open(r'html_v2/baike_' + t + '.html', 'w', encoding='utf-8') as f:
        f.write(content)

