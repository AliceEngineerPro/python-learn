from datetime import date
from datetime import timedelta

import pandas as pd


def add_month(d, md):  # 逐月追加算法
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    # return start(d.year + yd + yd, m, d.day)
    return date(d.year + yd + yd, m, d.day)

#
# from datetime import timedelta

books = pd.read_excel('D:/PyCharm/text_project/Excel_learn/read_excel/数字自动填充.xlsx', skiprows=3,
                      usecols='C:F', index_col=None,
                      dtype={'ID': str, 'InStore': str,
                             'Date': str})  # ,skiprows=3)-->从Excel的第4行开始读(除去前3行) # usecols='C:F')-->只读C到F列
# print(books)
# print(books['ID'])

# books['ID'].at[0]=100 # books中的Excel中“ID”这一列的填充，.at[第几列]=‘要填充的数据’
# print(books)

start = date(2018, 1, 1)
for i in books.index:
    books['ID'].at[i] = i + 1
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'
    # books['Date'].at[i] = date(start.year + i, start.month, start.day)  # 年加1
    books['Date'].at[i] = add_month(start, i)  # 月加1
    # books['Date'].at[i] = date = start + timedelta(days=i) # 天加1

    # books.at[i, 'ID'] = i + 1
    # books.at[i,'InStore'] = i + 1
    # books.at[i,'Date'] = add_month(start,i)

print(books)
# books.set_index('ID', inplace=True)
# books.to_excel('C:/Users/Amfc-/Desktop/1.xlsx')
print('Done!')
