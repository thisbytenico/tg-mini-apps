import openpyxl
import os

# 语言代码映射
lang_codes = {
    'zh-TW': 0,
    'en': 1,
    'zh-CN': 2,
    'ko': 3,
    'ja': 4,
    'vi': 5,
    'ru': 6,
    'tr': 7,
    'uk': 8,
    'es': 9,
    'pt': 10,
    'de': 11,
    'fr': 12,
    'fa': 13,
    'ar': 14,
    'nl': 15,
    'it': 16,
    'tl': 17,
    'id': 18,
    'bg': 19,
    'cs': 20,
    'da': 21,
    'el': 22,
    'pl': 23,
    'sl': 24,
    'hu': 25,
    'kk': 26,
    'lo': 27,
    'lv': 28,
    'ro': 29,
    'si': 30,
    'sk': 31,
    'sv': 32
}

# 读取Excel文件
wb = openpyxl.load_workbook('buy.xlsx')
sheet = wb.active

# 获取所有翻译行
translation_rows = []
for row in sheet.iter_rows(min_row=2, max_row=4, values_only=True):
    translation_rows.append(row)

# 读取原始HTML文件
with open('zh-TW.html', 'r', encoding='utf-8') as f:
    original_html = f.read()

# 为每种语言生成HTML文件
for lang_name, lang_index in lang_codes.items():
    # 构建翻译内容
    translation1 = translation_rows[0][lang_index]
    translation2 = translation_rows[1][lang_index]
    translation3 = translation_rows[2][lang_index]
    
    # 替换翻译内容
    translated_html = original_html
    translated_html = translated_html.replace(
        '因 <span style="font-weight:bold;">{{coinSymbol}}</span> 項目流動性不足，已無法維持正常交易。為保障您的資產安全與交易體驗，<span style="font-weight:bold;">KCEX已下架相關交易市場，並將對持幣戶進行回購。</span>',
        translation1
    )
    translated_html = translated_html.replace(
        '下架後，KCEX不再支持 <span style="font-weight:bold;">{{coinName}} ({{coinSymbol}})</span> 的充幣、提幣及交易服務',
        translation2
    )
    translated_html = translated_html.replace(
        '回購完成後，對應的USDT將會空投至您的帳戶。請至【錢包】→【交易記錄】→【其他 】查看空投紀錄，並留意資產變動。',
        translation3
    )
    
    # 生成文件名
    filename = f'{lang_name}.html'
    
    # 保存文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(translated_html)
    
    print(f'生成文件: {filename}')

print('所有文件生成完成！')