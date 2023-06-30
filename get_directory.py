import os


def get_top_level_directories(directory):
    directories = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            directories.append(item_path)
    return directories

# 指定路径,前端返回
path = 'your_path' 

# 获取下一级目录
top_level_directories = get_top_level_directories(path)

# 打印目录路径
for directory in top_level_directories:
    print(directory)
