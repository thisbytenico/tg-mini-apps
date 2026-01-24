import os

# 遍历html2目录下的所有HTML文件
for filename in os.listdir('html2'):
    if filename.endswith('.html'):
        html_path = os.path.join('html2', filename)
        
        # 读取HTML内容
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # 查找包含{{minValue}}的div标签（注意大小写）
        minvalue_start = html_content.find('{{minValue}}')
        if minvalue_start == -1:
            print(f'未找到{{minValue}}: {filename}')
            continue
        
        # 查找该div标签的开始位置
        div_start = html_content.rfind('<div', 0, minvalue_start)
        if div_start == -1:
            print(f'未找到div标签: {filename}')
            continue
        
        # 查找该div标签的父级p标签
        p_start = html_content.rfind('<p', 0, div_start)
        if p_start == -1:
            print(f'未找到父级p标签: {filename}')
            continue
        
        # 检查p标签是否已经有id
        p_end = html_content.find('>', p_start)
        if 'id="attention"' in html_content[p_start:p_end]:
            print(f'p标签已有id: {filename}')
            continue
        
        # 为p标签添加id="attention"
        new_html = html_content[:p_end] + ' id="attention"' + html_content[p_end:]
        
        # 保存文件
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print(f'已添加id: {filename}')

print('所有文件处理完成！')