import openpyxl

# 读取Excel文件
wb = openpyxl.load_workbook('buy.xlsx')
sheet = wb.active

# 打印前10行
print("Excel文件前10行内容：")
for i, row in enumerate(sheet.iter_rows(values_only=True)):
    if i >= 10:
        break
    print(f"行 {i+1} 长度: {len(row)}, 内容: {row}")