import xlrd

# 读取Excel文件
wb = xlrd.open_workbook('t_notifier_template_i18n_copy.xls')
sheet = wb.sheet_by_index(0)

# 打印表头
print("表头:")
for col_idx in range(sheet.ncols):
    print(f"列 {col_idx}: {sheet.cell_value(0, col_idx)}")

# 查找mail.spot.symbol.delisting的行
print("\n查找mail.spot.symbol.delisting的行:")
for row_idx in range(sheet.nrows):
    row = sheet.row_values(row_idx)
    if row[0] == 'mail.spot.symbol.delisting':
        print(f"找到行 {row_idx}")
        print(f"行长度: {len(row)}")
        print(f"行内容: {row}")
        break