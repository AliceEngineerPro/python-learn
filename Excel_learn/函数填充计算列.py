import pandas as pd


def add_2(x):
    return x + 2


books = pd.read_excel('D:/PyCharm/text_project/Excel_learn/read_excel/函数填充计算列.xlsx', index_col='ID')
# books['Price'] = books['Discount'] * books['ListPrice']

# for i in books.index:
#     books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]

# for i in range(5,16):
#     books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]

# books['ListPrice'] = books['ListPrice'] + 2  # 每‘ListPrice’列+2
# books['ListPrice'] = books['ListPrice'].apply(add_2) 调用函数add_2

books['ListPrice'] = books['ListPrice'].apply(lambda x: x + 2)  # lambda表达式

print(books)
