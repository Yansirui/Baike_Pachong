from bs4 import BeautifulSoup
import os
dir_path=os.listdir('/home/sirui/WMM/Medicine/Data/html_v3')
all_terms=[]
need_new_path=[]
all_contexts=[]
with open(r'/home/sirui/WMM/Medicine/baike_data/baike_corpus.txt') as f:
    for file in dir_path:
        html_path=r'/home/sirui/WMM/Medicine/Data/html_v3/'+file
        current_term=html_path.split('/')[-1].replace('baike_','').replace('.html','')
        all_terms.append(current_term)
        soup = BeautifulSoup(open(html_path,'r',encoding='utf-8'),'html.parser')
        if 'summary' not in soup.prettify():
            need_new_path.append(file)
            continue
        all_terms.append(soup.h1.string)
        context=[]
        for content in soup.find_all('div'):
            if content.get('class') == None:
                continue
            if 'MARK_MODULE' in content.get('class'):
                context.append(content.get_text())
        tongyici=''
        for same_term in soup.find_all('b'):
            if same_term.get('class') == None:
                continue
            else:
                if 'polysemant-list-lemma-title' in same_term.get('class'):
                    tongyici=same_term.string
        if tongyici == '':
            print('该词没有同义词')
        else:
            all_terms.append(tongyici)
        for con in context:
            con = con.replace('\n','')
            if con == '':
                continue
        all_contexts.append(''.join(context).replace('\n','').replace('\xa0',''))
        if len(all_contexts) % 500 == 0:
            for c in all_contexts:
                f.write(c+'\n')
            all_contexts=[]
with open(r'/home/sirui/WMM/Medicine/baike_data/terms.txt') as f:
    for term in all_terms:
        f.write(term+'\n')
with open(r'/home/sirui/WMM/Medicine/baike_data/renew_url.txt') as f:
    for url in need_new_path:
        f.write(url)
