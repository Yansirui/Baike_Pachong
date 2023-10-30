import re

def split_sentences(sentence):
    MAX_LENGTH = 500
    sentences = []
    sub_sentences=re.split(r'([。！!？?])',sentence)
    #sub_sentences.append("")
    #sub_sentences = ["".join(i) for i in zip(sentences[0::2],sentences[1::2])]
    #sub_sentences = sentence.split('，')
    cur_sentence = ''
    for sub in sub_sentences:
        if len(cur_sentence) + len(sub) > MAX_LENGTH:
            if cur_sentence != '':
                sentences.append(cur_sentence)
                cur_sentence = sub
            else:
                cur_sentence = sub
        else:
            cur_sentence += sub
    if cur_sentence != '':
        sentences.append(cur_sentence)
    return sentences
nums=1

with open(r'/home/sirui/WMM/Medicine/baike_data/baike_corpus.txt', 'r', encoding='utf-8') as f:
    save = []
    with open(r'/home/sirui/WMM/Medicine/baike_data/SCL_corpus.txt', 'w', encoding='utf-8') as f_save:
        sentences = (line.strip() for line in f)
        for sentence in sentences:
            if len(sentence) > 500:
                sub_sentences = split_sentences(sentence)
                for sub_sentence in sub_sentences:
                    if 500 > len(sub_sentence) > 8:
                        save.append(sub_sentence)
            elif 8 < len(sentence) <= 500:
                save.append(sentence)
            if len(save) % 1000 == 0:
                print('保存数目:', nums * 1000)
                nums = nums + 1
                for senn in save:
                    f_save.write(senn + '\n')
                save = []
        if len(save) > 0:
            for senn in save:
                f_save.write(senn + '\n')
