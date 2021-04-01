import pandas as pd

# d = {'x':100,'y':200,'z':300}
# print(d.values(),d.keys()) # 输出对应的键和值  ，d.keys() 字典中的键 d.values() 字典中的值
# print(d['x']) # 打印字典d 中‘x’键对应的值
# s1 = pd.Series(d)
# print(s1.index) # 打印字典d中的key

# L1 = [100,200,300]
# L2 = ['x','y','z']
#
# s1 = pd.Series(L1,index=L2)
# print(s1)


s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')
s4 = pd.Series([1000, 2000, 3000], index=[1, 2, 3], name='D')

# s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
# s2 = pd.Series([1, 2, 3], index=[10, 20, 30], name='B')
# s3 = pd.Series([1, 2, 3], index=[100, 200, 300], name='c')

df = pd.DataFrame({s1.name: s1,s2.name: s2, s3.name: s3,s4.name:s4})  # 用DataFrame要写成字典形式

# df = pd.DataFrame([s1,s2,s3])
print(df)
df.to_excel('F:\#!Python_porject\用餐信息数据清洗\总表\合并.xlsx',sheet_name='1',index=False)