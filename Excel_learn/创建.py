import pandas as pd

pf = pd.DataFrame()  # DataFrame 数据帧，格式：[‘第n列标题’：[数据用逗号隔开]]…………
#pf = pf.set_index('ID')  # 除去pandas中的自身索引的ID
pf.to_excel("C:/Users/Amfc-/Desktop/1.xlsx")  # 保存到（保存路径+文件名）下
print('done!')
