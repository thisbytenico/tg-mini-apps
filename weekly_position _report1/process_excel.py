import pandas as pd
import json

# 读取Excel文件
df = pd.read_excel('holdReport.xlsx')

# 获取第一行作为语言key
language_keys = df.columns.tolist()

# 获取第20行的数据（注意：pandas的索引从0开始，所以第20行是索引19）
row_20 = df.iloc[19].values.tolist()

# 生成字典变量
dict_var = {}
for i, key in enumerate(language_keys):
    if pd.notna(row_20[i]):
        dict_var[key] = str(row_20[i])
    else:
        dict_var[key] = ''

# 生成JavaScript代码
js_code = f'// 第20行字典变量\nconst dict20 = {json.dumps(dict_var, ensure_ascii=False, indent=2)};\n\n'

# 读取index.html文件
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 在当前指数字典后添加新的字典变量
insert_position = html_content.find('//当前指数字典')
if insert_position != -1:
    # 找到当前指数字典的结束位置
    end_position = html_content.find('\n\n', insert_position)
    if end_position != -1:
        # 在当前指数字典后插入新的字典变量
        new_html_content = html_content[:end_position+2] + js_code + html_content[end_position+2:]
        
        # 写入更新后的index.html文件
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_html_content)
        
        print('成功生成并添加第20行字典变量到index.html')
        print('生成的字典变量：')
        print(f'dict20: {dict_var}')
    else:
        print('未找到当前指数字典的结束位置')
else:
    print('未找到当前指数字典')
