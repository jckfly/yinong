import re
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk import pos_tag

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

import re
 
def remove_pronouns(text):
    # 正则表达式匹配人称代词
    # 这里仅列出了一些常见的人称代词，实际使用中需要根据需求进行扩展
    pronouns = [r"\b(I|we|he|she|it|they)\b", r"\b(me|us|him|her|it|them)\b", r"\b(my|our|his|her|its|their)\b"]
    pattern = "|".join(pronouns)
    
    # 使用正则表达式进行匹配并替换
    return re.sub(pattern, "", text)
 
# # 示例文本
# text = "She said that she would come back next week."
# # 去除文本中的人称代词
# clean_text = remove_pronouns(text)
# print(clean_text)











with open("Python.txt") as P:
    lines=P.readlines()
    for line  in lines:
        line.replace('\n',' ')
add={}
stop_words=set(stopwords.words('english'))

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

with open('aa.csv','a') as a:
    write=csv.writer(a)
    for j in add.keys():
       write.writerow([j,str(add[j])])
      
