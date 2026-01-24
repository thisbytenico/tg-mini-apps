import openpyxl
import os

# 语言代码映射
lang_code_map = {
    'ar-AE': 0,
    'bg-BG': 1,
    'cs-CZ': 2,
    'da-DK': 3,
    'de-DE': 4,
    'el-GR': 5,
    'en-US': 6,
    'es-ES': 7,
    'fa-IR': 8,
    'fil-PH': 9,
    'fr-FR': 10,
    'hu-HU': 11,
    'id-ID': 12,
    'it-IT': 13,
    'ja-JP': 14,
    'kk-KZ': 15,
    'ko-KR': 16,
    'lo-LA': 17,
    'lv-LV': 18,
    'nl-NL': 19,
    'pl-PL': 20,
    'pt-PT': 21,
    'ro-RO': 22,
    'ru-RU': 23,
    'si-LK': 24,
    'sk-SK': 25,
    'sl-SI': 26,
    'sv-FI': 27,
    'tr-TR': 28,
    'uk-UA': 29,
    'vi-VN': 30,
    'zh-TW': 31
}

# 读取buy.xlsx文件
wb_buy = openpyxl.load_workbook('buy.xlsx')
sheet_buy = wb_buy.active

# 获取第四行数据（索引从1开始）
row4 = sheet_buy[4]

# 遍历html2目录下的所有HTML文件
for filename in os.listdir('html2'):
    if filename.endswith('.html'):
        # 获取语言代码
        lang_code = filename[:-5]  # 去掉.html后缀
        
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
        
        # 查找p标签内部的第三个div标签
        div_count = 0
        div_start = attention_start
        while div_count < 3:
            div_start = html_content.find('<div', div_start)
            if div_start == -1 or div_start > p_end:
                break
            div_end = html_content.find('</div>', div_start)
            if div_end == -1:
                break
            div_count += 1
            if div_count == 3:
                break
            div_start = div_end + 6
        
        if div_count < 3:
            print(f'未找到第三个div标签: {filename}')
            continue
        
        # 获取替换内容
        if lang_code in lang_code_map:
            lang_index = lang_code_map[lang_code]
            replace_content = row4[lang_index + 1].value  # 从第二列开始是翻译内容
        else:
            print(f'未找到语言映射: {filename}')
            continue
        
        # 替换内容
        new_html = html_content[:div_start] + f'<div>{replace_content}</div>' + html_content[div_end+6:]
        
        # 保存文件
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print(f'已替换文件: {filename}')

print('所有文件替换完成！')