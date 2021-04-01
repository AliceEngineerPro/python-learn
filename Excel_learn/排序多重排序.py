import pandas as pd

Products = pd.read_excel('D:/PyCharm/text_project/Excel_learn/read_excel/排序多重排序.xlsx',index_col='ID')
# Products.sort_values(by='Worthy',inplace=True,ascending=False)  # ascending -->从小到大排序
Products.sort_values(by=['Worthy','Price'],inplace=True,ascending=[True,False])  # ascending -->从小到大排序

print(Products)
# Products.to_excel('C:/Users/Amfc-/Desktop/1.xlsx')
print('Dome')