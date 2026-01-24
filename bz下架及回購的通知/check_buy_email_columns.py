import xlrd

# 读取buyEmail.xls文件
wb = xlrd.open_workbook('buyEmail.xls')
sheet = wb.sheet_by_index(0)

# 打印第一行的列标题
print('buyEmail.xls的列标题:')
for col_idx in range(sheet.ncols):
    print(f'列{col_idx+1}: {sheet.cell(0, col_idx).value}')

# 打印前几行的内容
print('\n前5行的内容:')
for row_idx in range(min(5, sheet.nrows)):
    row_content = []
    for col_idx in range(sheet.ncols):
        row_content.append(str(sheet.cell(row_idx, col_idx).value))
    print(f'行{row_idx+1}: {" | ".join(row_content)}')