from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import json
#百度健康所有疾病和症状爬取 Selenium
terms=[]
same=[]
browser = webdriver.Edge(r"D:\Microsoft\msedgedriver.exe")
browser.get('https://jiankang.baidu.com/widescreen/entitylist?tabType=1&navType=1/')
e1 = browser.find_element('xpath', '//*[contains(text(), "查疾病")]')

action_chains = ActionChains(browser)
action_chains.click(e1).perform()
time.sleep(1)
element = browser.find_element('xpath', '//*[contains(text(), "按科室")]')
action_chains.click(element).perform()
time.sleep(1)
pattern=r'<div class="_3jQHe">.*?</div>'
elements = browser.find_elements('xpath','//*[contains(text(), "科")]')
for element in elements:
    print('---------------------------------------')
    print(element.text)
    for i in range(10):
        print(i)
        if '科室' in element.text or element.text=='':
            break
        action_chains.click(element).perform()
        html_content=browser.page_source
        word_differs=re.findall(pattern,html_content)
        for word_differ in word_differs:
            has_found=False
            all_terms=re.findall(r'<a href.*?</a>',word_differ)
            for term in all_terms:
                dict_term={
                    'term':re.search(r'<a.*?>(.*?)</a>',term).group(1),
                    '科室':element.text
                }
                if re.search(r'<a.*?>(.*?)</a>',term).group(1) in same:
                    has_found=True
                    break
                terms.append(dict_term)
                same.append(re.search(r'<a.*?>(.*?)</a>',term).group(1))
            if has_found:
                break
        time.sleep(1)
print(len(terms))

e2 = browser.find_element('xpath', '//*[contains(text(), "查症状")]')
action_chains = ActionChains(browser)
action_chains.click(e2).perform()
time.sleep(3)
element = browser.find_element('xpath', '//*[contains(text(), "按科室")]')
action_chains.click(element).perform()
time.sleep(3)
pattern=r'<div class="_3jQHe">.*?</div>'
elements = browser.find_elements('xpath','//*[contains(text(), "科")]')
for element in elements:
    print(element.text)
    for i in range(10):
        if '科室' in element.text or element.text=='':
            break
        action_chains.click(element).perform()
        html_content=browser.page_source
        word_differs=re.findall(pattern,html_content)
        for word_differ in word_differs:
            has_found=False
            all_terms=re.findall(r'<a href.*?</a>',word_differ)
            for term in all_terms:
                dict_term={
                    'term':re.search(r'<a.*?>(.*?)</a>',term).group(1),
                    '科室':element.text
                }
                if re.search(r'<a.*?>(.*?)</a>', term).group(1) in same:
                    has_found = True
                    break
                terms.append(dict_term)
                same.append(re.search(r'<a.*?>(.*?)</a>', term).group(1))
            if has_found:
                break
        time.sleep(1)
print('百度健康词汇：',len(terms))
#百度百科健康医疗相关词条爬取，显示有4w，拉到最下面只有200个左右，所以需要自己做词汇扩展
browser.get('https://baike.baidu.com/wikitag/taglist?tagId=76625')
for i in range(20):
    browser.execute_script('window.scrollBy(0,1000)')
    time.sleep(1)
elements=browser.find_elements('class name','front')

for e in elements:
    terms.append({
        'term':e.text.split('\n')[0],
        'category':''
    })
print(len(terms))
with open(r'terms_v1.json', 'w', encoding='utf-8') as f:
    json.dump(terms, f, ensure_ascii=False, indent=2)
browser.quit()
