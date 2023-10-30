import requests
#看v1版本里的item是否和医疗有关

n=0
with open(r'/home/sirui/WMM/Medicine/Data/item扩展_v4.txt','r',encoding='utf-8') as f:
    items=f.readlines()[n*80000:80000*(1+n)]
new_urls=[]
for i in range(len(items)):
    items[i].replace('\n','')
print(len(items))
i=1
terms=[]
index = 0
with open(r'/home/sirui/WMM/Medicine/Data/item扩展_v5_'+str(n)+'.txt','w',encoding='utf-8') as f:
    for url in items:
        index = index + 1
        if index % 1000 == 0:
            print('已经看了{}个url'.format(index))
        item_url = url.replace('\n','')
        term = item_url.split('/')[4].replace('\n','')
        response=requests.get(item_url)
        content=response.text
        times = 0
        while '百度百科-验证' in content:
            if times == 5:
                break
            content = requests.get(url).text
            times = times + 1
        if '百度百科-验证' in content:
            continue
        if '疾病' in content or '科室' in content or '病症' in content :
            if term not in terms:
                terms.append(term)
                new_urls.append(item_url+'\n')
                with open(r'/home/sirui/WMM/Medicine/Data/html_v3/baike_' + term + '.html', 'w', encoding='utf-8') as f1:
                    f1.write(content)
            else:
                continue
            if len(new_urls) % 50 == 0:
                for url1 in new_urls:
                    f.write(url1)
                print('保存url数目:', i * 50)
                new_urls=[]
                i=i+1
    if len(new_urls) > 0:
        for url1 in new_urls:
            f.write(url1)


#v2版本会有重复的词条以及部分与医疗无关，二度筛选
'''
with open(r'item扩展_v4.txt','r',encoding='utf-8') as f:
    items=f.readlines()
terms=[]
terms_url=[]
for item in items:
    if 'viewPageContent' in item:
        continue
    else:
        item = item.replace('\n','')
        term = item.split('/')[4]
        if term not in terms:
            terms.append(term)
            terms_url.append(item)
        else:
            continue
with open(r'item扩展_v3.txt','w',encoding='utf-8') as f:
    for term in terms_url:
        f.write(term+'\n')
'''