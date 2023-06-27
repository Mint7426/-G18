'''
    #利用python查找word文档中的关键词，支持多个文档和多个关键词
'''
# 导入所需库
import os,re
from docx import Document
global ur
 
ur = "" #里面为路径相关
# key_word = '模糊查询' #全局变量读取关键字
 
 
def get_doc_path (path) :
    file_list = os.listdir(path)
    # 正则匹配路径下所有.docx结尾的文件
    doc_list = [i for i in file_list if re.compile(r'\w+.docx').match(i)]
    #拼接ur进入doc_list，获得完整路径
    for i in range(len(doc_list)):
        doc_list[i] = ur + '/' + doc_list[i]
    return doc_list
#以段落为单位切片，并查找关键字
def find_text (path,word):
    document = Document(path)
    all_paragraphs = document.paragraphs
    list1 = []
    for paragraph in all_paragraphs:
 
        str1 = paragraph.text
        if str1.find(word) != -1 :
            list1.append(str1)
    if list1 == [] :
        list1.append('未找到关键字')
    return list1
        # else:print('notfind')
 
 
#获取路径下txt中的关键字并返回一个list
def read_keyword (add) :
    with open(add+'/key_word.txt',encoding='utf=8') as f :
        key_word = f.readlines()
        for i in range(len(key_word)) :
            key_word[i] = key_word[i].strip()#去除换行符
        return key_word
 
 
 
key_word = read_keyword(ur)
print(key_word)
doc_path = get_doc_path(ur)
print(doc_path)
list_word = []
document = Document()
for x in doc_path :
    document.add_heading(x,level=1)
    for i in key_word :
        document.add_paragraph(i , style='Intense Quote')
        for num in range(len(find_text(x,i))):
            no = num+1
            str(no)
            str1 = 'NO.' + str(no)
            document.add_paragraph(str1)#添加标号
            document.add_paragraph(find_text(x,i)[num])#写入正文
document.save(ur + '/result.docx')
