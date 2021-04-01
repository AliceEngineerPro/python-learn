# 函数
def functions(x):
    """
    functions test
    """
    x += 1
    y = x ** 2
    return x, y


functions = functions(x=5)
# print(functions)


"""
def: 定义函数的关键字
function: 函数名
(): 参数,多个参数用逗号隔开
x += 1, y = x**2: 代码块的处理逻辑
return: 定义返回值
"""


# 例子
def function_1():
    # num = int(input('请输入密码:'))
    num = 123
    yes = '密码正确!'
    no = '密码错误,请重新输入!'
    if num != 123:
        return no
    return yes


function_1 = function_1()
print(function_1)


# 函数参数
# 形参


def function_2(x, y):
    count_2 = x**y
    return count_2


function_2 = function_2(1, 2)
print(function_2)

