import os

index_file = "file_index.txt"
selected_results = []


# 建立文件索引
def build_file_index(directory):
    with open(index_file, "w") as file:
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_type = get_file_type(file_name)
                if file_type in ['pdf', 'word']:
                    file_info = f"{file_name}\t{file_path}\t{file_type}\n"
                    file.write(file_info)


def get_file_type(file_name):  # 获取文件类型
    # 根据文件名后缀判断文件类型
    file_extension = os.path.splitext(file_name)[1].lower()
    if file_extension == '.pdf':
        return 'pdf'
    elif file_extension in ['.doc', '.docx']:
        return 'word'
    else:
        return 'other'

build_file_index("D:\A学习\填报的表格")