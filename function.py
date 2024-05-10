import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk
import csv
nltk.download('stopwords')
nltk.download('punkt') 
nltk.download('averaged_perceptron_tagger')
stop_words=set(stopwords.words('english'))
 
def remove_pronouns(text):#对人称代词的移除
    # 正则表达式匹配人称代词
    # 这里仅列出了一些常见的人称代词，实际使用中需要根据需求进行扩展
    pronouns = [r"\b(I|we|he|she|it|they)\b", r"\b(me|us|him|her|it|them)\b", r"\b(my|our|his|her|its|their)\b"]
    pattern = "|".join(pronouns)
    
    # 使用正则表达式进行匹配并替换
    return re.sub(pattern, "", text)
def open_the_text(filename='Python.txt'):#打开文本
    with open(file=filename) as P:
        lines=P.readlines()
        for line  in lines:
            line.replace('\n',' ')
    return lines
def computer_word(lines):
    add={}
    for line in lines:
        line.strip()
    
        line=re.sub(r'\n+',' ',line)#去除制表符号
        # line=re.sub(r'\?\s*','',line)
        # line=re.sub(r'\s*-\s*','',line)
        # line=re.sub(r'[^\x20-\x7E]','',line)
        # line=re.sub(',','',line)
        # line=re.sub(r'!','',line)
        line=re.sub(r'[^\w\s]',' ',line)#将不是字母的符号移除
        line=line.lower()
        line=remove_pronouns(line)
        # line=re.sub(r'[^\w\s]','',line)
        # if line is '\n':
        #     continue
        m=line.split(" ")#将一行变成列表
    
        token=word_tokenize(line)#标记文本
        #tag=pos_tag(token)
        #print(tag)
        m_filtered_tokens=[w for w in token if w not in stop_words]#去除虚词
        m=m_filtered_tokens
        for i in m:
            if i in add.keys():
                add[i]+=1
            else :add[i]=1
    return add
def store_csv(word):
    with open('aa.csv','a') as a:
        write=csv.writer(a)
        for j in word.keys():
             write.writerow([j,str(word[j])])
def dict2list(dict):
    values=[]
    for i in dict.keys():
        values.append((i,dict[i]))
        return values

def store_databases(word,corsor,connect):
    values=dict2list(word)
    sql='insert ignore into word values(%s,%s)'
    corsor.executemany(sql,values)
    connect.commit()


