import xlrd

# 读取buyEmail.xls文件
wb = xlrd.open_workbook('buyEmail.xls')
sheet = wb.sheet_by_index(0)

# 打印第一行的列标题
print('buyEmail.xls的列标题:')
for col_idx in range(sheet.ncols):
    print(f'列{col_idx+1}: {repr(sheet.cell(0, col_idx).value)}')