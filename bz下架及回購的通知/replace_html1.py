import openpyxl
import xlrd
import os

# 语言代码映射
lang_code_map = {
    'ar-AE': 'ar',
    'bg-BG': 'bg',
    'cs-CZ': 'cs',
    'da-DK': 'da',
    'de-DE': 'de',
    'el-GR': 'el',
    'en-US': 'en',
    'es-ES': 'es',
    'fa-IR': 'fa',
    'fil-PH': 'tl',
    'fr-FR': 'fr',
    'hu-HU': 'hu',
    'id-ID': 'id',
    'it-IT': 'it',
    'ja-JP': 'ja',
    'kk-KZ': 'kk',
    'ko-KR': 'ko',
    'lo-LA': 'lo',
    'lv-LV': 'lv',
    'nl-NL': 'nl',
    'pl-PL': 'pl',
    'pt-PT': 'pt',
    'ro-RO': 'ro',
    'ru-RU': 'ru',
    'si-LK': 'si',
    'sk-SK': 'sk',
    'sl-SI': 'sl',
    'sv-FI': 'sv',
    'tr-TR': 'tr',
    'uk-UA': 'uk',
    'vi-VN': 'vi',
    'zh-TW': 'zh-TW'
}

# 读取buy.xlsx文件
wb_buy = openpyxl.load_workbook('buy.xlsx')
sheet_buy = wb_buy.active

# 获取第四行数据（索引从1开始）
row4 = sheet_buy[4]

# 读取t_notifier_template_i18n_copy.xls文件
wb_template = xlrd.open_workbook('t_notifier_template_i18n_copy.xls')
sheet_template = wb_template.sheet_by_index(0)

# 处理每个语言文件
for row_idx in range(sheet_template.nrows):
    row = sheet_template.row_values(row_idx)
    if row[0] == 'mail.spot.symbol.delisting':
        lang_code = row[1]
        # 转换语言代码
        if lang_code in lang_code_map:
            target_lang = lang_code_map[lang_code]
        else:
            target_lang = lang_code
        
        # 读取html1目录下的文件
        html_path = os.path.join('html1', f'{target_lang}.html')
        if not os.path.exists(html_path):
            print(f'跳过不存在的文件: {html_path}')
            continue
        
        # 读取HTML内容
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # 查找第四个p标签
        p_count = 0
        start_idx = 0
        while p_count < 4:
            p_start = html_content.find('<p', start_idx)
            if p_start == -1:
                break
            p_end = html_content.find('</p>', p_start)
            if p_end == -1:
                break
            p_count += 1
            start_idx = p_end + 4
        
        if p_count < 4:
            print(f'未找到第四个p标签: {html_path}')
            continue
        
        # 查找第三个div标签
        div_count = 0
        div_start = start_idx
        while div_count < 3:
            div_start = html_content.find('<div', div_start)
            if div_start == -1:
                break
            div_end = html_content.find('</div>', div_start)
            if div_end == -1:
                break
            div_count += 1
            if div_count == 3:
                break
            div_start = div_end + 6
        
        if div_count < 3:
            print(f'未找到第三个div标签: {html_path}')
            continue
        
        # 获取替换内容
        lang_index = list(lang_code_map.values()).index(target_lang)
        replace_content = row4[lang_index + 1]  # 从第二列开始是翻译内容
        
        # 替换内容
        new_html = html_content[:div_start] + f'<div>{replace_content}</div>' + html_content[div_end+6:]
        
        # 保存文件
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print(f'已替换文件: {html_path}')

print('所有文件替换完成！')