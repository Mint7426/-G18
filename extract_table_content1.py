import docx


# 处理docx文件中含有合并单元格
# 方法一：从前往后查找和从后往前查找，索引不同而地址相同则为合并单元格
def extract_table_content(doc_path):
    doc = docx.Document(doc_path)
    table_contents = []
    for table in doc.tables:
        table_data = []
        cells = table._cells
        rows = table.rows
        cols = table.columns
        for i, cell in enumerate(cells):
            if cell in cells[:i]: # 如果该单元格不是在表中第一次出现则跳过
                continue
            for j in range(len(rows)):
                if i >= j * len(cols) and i < (j+1) * len(cols):
                    row_index = j
                    col_index = i % len(cols)
                    break
            cell_text = cell.text
            if is_merged_cell(cells, i): # 判断是否为合并单元格
                cell_text = ''
            while len(table_data) <= row_index:
                table_data.append([])
            table_data[row_index].append(cell_text)
        
        table_contents.append(table_data)
    
    for table_data in table_contents:
        for row in table_data:
            print('\t'.join(row))


def is_merged_cell(cells, index):
    cell = cells[index]
    for i in range(index - 1, -1, -1):  # 倒序查找
        if cell is cells[i]:  # 找到"相同"的单元格，如果没有"合并"单元格，则会倒序找到"自己"
            return True
    return False


# 将docx文件路径传递给以下函数调用
extract_table_content('new.docx')
