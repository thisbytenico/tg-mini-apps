import os

# 遍历html2目录下的所有HTML文件
for filename in os.listdir('html2'):
    if filename.endswith('.html'):
        # 读取HTML内容
        html_path = os.path.join('html2', filename)
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # 查找id为attention的p标签
        attention_start = html_content.find('id="attention"')
        if attention_start == -1:
            print(f'未找到id为attention的p标签: {filename}')
            continue
        
        # 查找p标签的结束位置
        p_end = html_content.find('</p>', attention_start)
        if p_end == -1:
            print(f'未找到p标签的结束位置: {filename}')
            continue
        
        # 查找p标签内部的第二个div标签
        div_count = 0
        div_start = attention_start
        while div_count < 2:
            div_start = html_content.find('<div', div_start)
            if div_start == -1 or div_start > p_end:
                break
            div_end = html_content.find('</div>', div_start)
            if div_end == -1:
                break
            div_count += 1
            if div_count == 2:
                break
            div_start = div_end + 6
        
        if div_count < 2:
            print(f'未找到第二个div标签: {filename}')
            continue
        
        # 检查div标签是否已经有id
        div_tag_end = html_content.find('>', div_start)
        if 'id="attention1"' in html_content[div_start:div_tag_end]:
            print(f'div标签已有id: {filename}')
            continue
        
        # 为div标签添加id="attention1"
        new_html = html_content[:div_tag_end] + ' id="attention1"' + html_content[div_tag_end:]
        
        # 保存文件
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print(f'已添加id: {filename}')

print('所有文件处理完成！')