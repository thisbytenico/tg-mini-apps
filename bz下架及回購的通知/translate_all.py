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
    'zh-Hant': 'zh-TW',
    'zh-Hans': 'zh-CN'
}

# 读取Excel文件
wb = xlrd.open_workbook('t_notifier_template_i18n_copy.xls')
sheet = wb.sheet_by_index(0)

# 查找mail.spot.symbol.delisting的所有行
translations = {}
for row_idx in range(sheet.nrows):
    row = sheet.row_values(row_idx)
    if row[0] == 'mail.spot.symbol.delisting':
        lang_code = row[1]
        # 转换语言代码
        if lang_code in lang_code_map:
            lang_code = lang_code_map[lang_code]
        translations[lang_code] = row[3]

# 定义需要替换的中文词条
chinese_texts = {
    '尊敬的 KCEX 用戶：': 'greeting',
    '回購詳情': 'buyback_details',
    'KCEX 將以 {{coinPrice}} USDT（最終成交價）回購 {{coinName}} ({{coinSymbol}})。': 'buyback_info',
    '注意事項': 'notes',
    '持有代币價值低於 {{minValue}} USDT 的用戶，將統一按 {{minValue}} USDT 進行空投。': 'min_value',
    '如有任何疑問，歡迎隨時聯繫客服團隊。': 'contact'
}

# 处理每种语言
for lang_code, translated_content in translations.items():
    # 读取原始HTML文件
    html_path = os.path.join('html', f'{lang_code}.html')
    if not os.path.exists(html_path):
        print(f'跳过不存在的文件: {html_path}')
        continue
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 提取翻译内容
    translated_parts = {}
    
    # 提取问候语
    greeting_start = translated_content.find('<p style="font-family: DIN Pro,\'Open Sans\', sans-serif;font-size: 18px;color: #151617;font-weight: bold;margin-bottom: 16px;">')
    if greeting_start != -1:
        greeting_start += len('<p style="font-family: DIN Pro,\'Open Sans\', sans-serif;font-size: 18px;color: #151617;font-weight: bold;margin-bottom: 16px;">')
        greeting_end = translated_content.find('</p>', greeting_start)
        translated_parts['greeting'] = translated_content[greeting_start:greeting_end].strip()
    
    # 提取回购详情
    buyback_details_start = translated_content.find('<div style="font-weight:bold;">')
    if buyback_details_start != -1:
        buyback_details_start += len('<div style="font-weight:bold;">')
        buyback_details_end = translated_content.find('</div>', buyback_details_start)
        translated_parts['buyback_details'] = translated_content[buyback_details_start:buyback_details_end].strip()
    
    # 提取回购信息
    buyback_info_start = translated_content.find('KCEX 將以')
    if buyback_info_start == -1:
        buyback_info_start = translated_content.find('KCEX will buy back')
    if buyback_info_start == -1:
        buyback_info_start = translated_content.find('KCEX 回购')
    if buyback_info_start != -1:
        buyback_info_end = translated_content.find('</div>', buyback_info_start)
        translated_parts['buyback_info'] = translated_content[buyback_info_start:buyback_info_end].strip()
    
    # 提取注意事项
    notes_start = translated_content.find('注意事項')
    if notes_start == -1:
        notes_start = translated_content.find('Notes')
    if notes_start == -1:
        notes_start = translated_content.find('注意事项')
    if notes_start != -1:
        notes_end = translated_content.find('</div>', notes_start)
        translated_parts['notes'] = translated_content[notes_start:notes_end].strip()
    
    # 提取最低价值
    min_value_start = translated_content.find('持有代币價值低於')
    if min_value_start == -1:
        min_value_start = translated_content.find('If the value of your tokens')
    if min_value_start == -1:
        min_value_start = translated_content.find('持有代币价值低于')
    if min_value_start != -1:
        min_value_end = translated_content.find('</div>', min_value_start)
        translated_parts['min_value'] = translated_content[min_value_start:min_value_end].strip()
    
    # 提取联系信息
    contact_start = translated_content.find('如有任何疑問')
    if contact_start == -1:
        contact_start = translated_content.find('If you have any questions')
    if contact_start == -1:
        contact_start = translated_content.find('如有任何疑问')
    if contact_start != -1:
        contact_end = translated_content.find('</p>', contact_start)
        translated_parts['contact'] = translated_content[contact_start:contact_end].strip()
    
    # 替换HTML内容
    for original_text, key in chinese_texts.items():
        if key in translated_parts:
            html_content = html_content.replace(original_text, translated_parts[key])
    
    # 保存翻译后的HTML文件
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f'已翻译文件: {html_path}')

print('所有文件翻译完成！')