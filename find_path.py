# coding=gbk
# 查找文件所在路径参考代码
import sys,os,re

def spider(script_path,script_type):
    final_files = []
    for root, dirs, files in os.walk(script_path, topdown=False):
            for fi in files:
                dfile = os.path.join(root, fi)
                if dfile.endswith(script_type):
                    final_files.append(dfile.replace("\\","/"))
    print("[+] 共找到了 {} 个word文件".format(len(final_files)))
    return final_files

def scanner(files_list,cmd):
    for item in files_list:
        fp = open(item, "r",encoding="utf-8")
        data = fp.readlines()
        for line in data:
            Code_line = data.index(line) + 1
            Now_code = line.strip("\n")
            for unsafe in [cmd]:
                flag = re.findall(unsafe, Now_code)
                if len(flag) != 0:
                    print("关键字： {} --行号: {} --文件路径: {} " .\
                          format(flag,Code_line,item))

if __name__ == "__main__":
    path = sys.argv[1]
    shell = sys.argv[2]
    ret = spider(path,".word")
    scanner(ret,shell)
