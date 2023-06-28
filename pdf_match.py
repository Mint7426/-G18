import os
import PyPDF2
from docx import Document


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


# 关键字查询
def search_keywords(keywords):
    matching_results = []
    with open(index_file, "r") as file:
        current_file_path = None
        line_number = 0
        for line in file:
            file_name, file_path, file_type = line.strip().split('\t')
            if file_type in ['pdf', 'word']:
                if current_file_path != file_path:
                    current_file_path = file_path
                    line_number = 0
                else:
                    line_number += 1
                matches = find_keyword_matches(keywords, file_name, file_path, line_number)
                matching_results.extend(matches)
    return matching_results


# 在文件中查找关键字匹配
def find_keyword_matches(keywords, file_name, file_path, line_number):
    matches = []
    # pdf处理
    if file_path.endswith('.pdf'):
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            page_number = 0
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text = page.extract_text()
                lines = text.split('\n')
                for line in lines:
                    line_number += 1
                    if any(keyword in line for keyword in keywords):
                        match = (file_path, line_number, line.strip())
                        matches.append(match)
    # word处理(有误，只能处理一个文件)
    elif file_path.endswith('.docx'):
        try:
            document = Document(file_path)
            paragraph_number = 0
            for paragraph_number, paragraph in enumerate(document.paragraphs, 1):
                line_number += 1
                if any(keyword in paragraph.text for keyword in keywords):
                    match = (file_path, line_number, paragraph.text.strip())
                    matches.append(match)
        except Exception as e:
            print(f"Error occurred while processing '{file_name}': {e}")
    return matches


# 用户选择结果(默认全部)
def select_result(result):
    selected_results.append(result)


# 用户保存结果到文件
def save_results_to_file():
    if not selected_results:
        print("No result.")
        return
    
    with open("saved_results.txt", "w") as file:
        current_file_path = None
        for file_path, line_number, content in selected_results:
            if current_file_path != file_path:
                current_file_path = file_path
                file.write(f"{file_path}\n{'-' * 30}\n")
            file.write(f"行号{line_number}\t{content}\n")
    
    print("Saved as saved_results.txt")


# 主程序 需要前端提供 directory与keywords
def main():
    directory = "D:\A学习\填报的表格"
    keywords = ["2020", "学校", "信息", "204"]
    build_file_index(directory)
    search_results = search_keywords(keywords)
    for result in search_results:
        select_result(result)
    save_results_to_file()


main()
