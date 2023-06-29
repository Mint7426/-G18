import docx
from lxml import etree


# 处理docx文件中含有合并单元格
# 方法二：借助lxml库来处理复杂表格
def extract_table_content(doc_path):
    doc = docx.Document(doc_path) # 读取表格
    tables = doc.tables # 获取所有的表格对象
    table = tables[0] # 获取第一个表格
    table_xml = table._element.xml # 获取表格XML
    table_root = etree.fromstring(table_xml) # 将XML转换为Element对象
    table_rows = table_root.xpath('.//w:tr', namespaces=table_root.nsmap) # 获取所有行
    table_data = []

    for i, row in enumerate(table_rows):
        row_data = []
        for cell in row:
            cell_text = ''
            for para in cell.iterdescendants('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                cell_text += para.text if para.text else ''
            row_data.append(cell_text)
        table_data.append(row_data)
    for row in table_data:
        print('\t'.join(row))
        

# 将docx文件路径传递给以下函数调用
extract_table_content('new.docx')