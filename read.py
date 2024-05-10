from function import *
from Setting import Setting
setting=Setting()
setting.connect()
connect,corsor=setting.get_db_corsor()
# # 示例文本
# text = "She said that she would come back next week."
# # 去除文本中的人称代词
# clean_text = remove_pronouns(text)
# print(clean_text)
text=open_the_text()
number=computer_word(text)
store_csv(number)



      
