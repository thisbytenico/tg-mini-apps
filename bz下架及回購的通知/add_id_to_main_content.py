import os

# 遍历html2目录下的所有HTML文件
html_dir = 'html2'
for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        # 读取HTML文件
        file_path = os.path.join(html_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # 查找id为mainContentCoin的标签
        main_content_coin_tag = 'id="mainContentCoin"'
        tag_index = html_content.find(main_content_coin_tag)
        
        if tag_index == -1:
            print(f'未找到id为mainContentCoin的标签: {filename}')
            continue
        
        # 查找该标签的父级p标签
        # 从tag_index向前查找最近的<p标签
        p_start = html_content.rfind('<p', 0, tag_index)
        if p_start == -1:
            print(f'未找到父级p标签: {filename}')
            continue
        
        # 查找p标签的结束位置（>符号）
        p_end = html_content.find('>', p_start)
        if p_end == -1:
            print(f'未找到p标签的结束符号: {filename}')
            continue
        
        # 检查p标签是否已经有id属性
        if 'id="' in html_content[p_start:p_end]:
            print(f'p标签已经有id属性: {filename}')
            continue
        
        # 为p标签添加id="mainContent"
        new_html = html_content[:p_end] + ' id="mainContent"' + html_content[p_end:]
        
        # 保存修改后的HTML
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print(f'已更新: {filename}')

print('所有文件处理完成！')