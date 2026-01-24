import os
import openpyxl

# 读取buy.xlsx文件
wb = openpyxl.load_workbook('buy.xlsx')
sheet = wb.active

# 获取第一行的语言标识（列标题）
lang_codes = [cell.value for cell in sheet[1]]

# 获取第三行的内容
row3 = [cell.value for cell in sheet[3]]

# 创建语言到内容的映射
translation_map = {}
for lang, content in zip(lang_codes, row3):
    if lang and content:
        translation_map[lang] = content

# 遍历html2目录下的所有HTML文件
html_dir = 'html2'
for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        # 提取文件名中的语言代码（如zh-TW.html -> zh-TW）
        file_lang = filename[:-5]  # 去掉.html后缀
        
        # 查找对应的翻译内容
        if file_lang in translation_map:
            target_content = translation_map[file_lang]
            
            # 读取HTML文件
            file_path = os.path.join(html_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # 查找id为attention1的div标签
            start_tag = '<div id="attention1">'
            end_tag = '</div>'
            
            start_index = html_content.find(start_tag)
            if start_index == -1:
                print(f'未找到id为attention1的div标签: {filename}')
                continue
            
            end_index = html_content.find(end_tag, start_index + len(start_tag))
            if end_index == -1:
                print(f'未找到id为attention1的div标签的结束标签: {filename}')
                continue
            
            # 替换div标签内的内容
            new_html = html_content[:start_index + len(start_tag)] + target_content + html_content[end_index:]
            
            # 保存修改后的HTML
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_html)
            
            print(f'已更新: {filename}')
        else:
            print(f'未找到对应的翻译内容: {filename}')

print('所有文件处理完成！')