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

# 创建html1目录
if not os.path.exists('html1'):
    os.makedirs('html1')

# 读取Excel文件
wb = xlrd.open_workbook('t_notifier_template_i18n_copy.xls')
sheet = wb.sheet_by_index(0)

# 查找mail.spot.symbol.delisting的所有行
for row_idx in range(sheet.nrows):
    row = sheet.row_values(row_idx)
    if row[0] == 'mail.spot.symbol.delisting':
        lang_code = row[1]
        # 转换语言代码
        if lang_code in lang_code_map:
            lang_code = lang_code_map[lang_code]
        
        # 生成HTML文件
        html_content = row[3]
        html_path = os.path.join('html1', f'{lang_code}.html')
        
        # 保存文件
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f'已生成文件: {html_path}')

print('所有文件生成完成！')