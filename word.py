import docx2txt
import re

#获取地址
path = "D:/testpy/a.docx"
#获取关键字
word = "你好"
#截取的最大字符数为12
num = 2
my_text=docx2txt.process(path)
#存储行号以及对应字符串的字典
textdict = {0: "0"}
#将docx转为文本
for num, string in enumerate(my_text.split("\n")):
    # print(num,repr(string))
    textdict[num] = repr(string)
#输出行号及其对应字符串
print(textdict)
#循环遍历查找关键字
for key,value in textdict.items():
    if(word in value):
        for m in re.finditer(word,value):
            start=m.start()
            end=m.end()
            #判断关键字位于哪个位置
            #关键字位于开头
            if m.start()-num<0:
                start=0
                #打印输出结果
                txt = value[0:end+num]
                print(key+1)
                print(txt)
            #关键字位于结尾
            elif m.end()+num>len(value):
                end=len(value)-1
                txt = value[start-num:end]
                print(key+1)
                print(txt)
            else:
                txt = value[start-num:end+num]
                print(key+1)
                print(txt)
#获得表格
document = Document(path)
tables = document.tables




