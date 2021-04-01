import pandas as pd

people = pd.read_excel("F:\#!Python_porject\text_porject_python\Excel_learn\read_excel\读查.xlsx",header=None)  # ,header=None) #>不设置header # ,header=1) #>第n行杂数据
print(people.shape)  # 显示总行总列
# print(people.columns)  # 显示第一行的标题
# 自定义行的标题并打印输出
# people.columns = ['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName']
# people.set_index('ID', inplace=True) # 删除pandas的自带索引
# print(people.columns)
# print(people.head(3)) #打印从头起（除标题）第n行的数据
# print('========================')
# print(people.tail(3)) #打印从尾部数第n行的数据
# people.to_excel("C:/Users/Amfc-/Desktop/1.xlsx")  # 输出到（‘文件’+'路径'）
# print('done!')

# df = pd.read_excel('C:/Users/Amfc-/Desktop/1.xlsx') # ,index_col='ID') # 用index_col='指定第一列'
# df.to_excel('C:/Users/Amfc-/Desktop/2.xlsx') # 生成文件（‘路径’+‘文件名’）
print('Done!')
