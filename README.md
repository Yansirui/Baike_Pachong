# Baike_Pachong
爬取的总体流程为：获取词汇(当前爬取为医疗领域的词条与数据，所以用selenium对百度健康和百科医疗领域词条进行爬取以获取第一个版本的词表) -->  百科数据获取(实现将网页内容保存下载，以便后续离线处理) -->  词汇扩展(根据已爬取的网页内容，找到该网页内容中有链接的所有词条，在百度百科中，有链接的词都是在百度百科中作为独立词条存在) -->  item筛选(根据自己所作领域去筛选词表，比如医疗领域选择疾病、症状等是否在网页中文中出现，如果出现就可以认为该词是与医疗领域相关) -->  循环百科数据获取到item筛选，当词表数量足够后，便可以获取正文之后分句处理，因为模型有输入限制，可以根据不同的输入限制去对爬取的正文部分进行分句。
