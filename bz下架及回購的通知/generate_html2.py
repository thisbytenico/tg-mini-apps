import xlrd
import os

# 创建html2目录
if not os.path.exists('html2'):
    os.makedirs('html2')

# 读取Excel文件
wb = xlrd.open_workbook('t_notifier_template_i18n_copy.xls')
sheet = wb.sheet_by_index(0)

# 查找mail.spot.symbol.delisting的所有行
for row_idx in range(sheet.nrows):
    row = sheet.row_values(row_idx)
    if row[0] == 'mail.spot.symbol.delisting':
        lang_code = row[1]
        
        # 生成HTML文件
        html_content = row[3]
        html_path = os.path.join('html2', f'{lang_code}.html')
        
        # 保存文件
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f'已生成文件: {html_path}')

print('所有文件生成完成！')