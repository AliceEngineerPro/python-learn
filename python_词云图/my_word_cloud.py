# ##对于NLP（自然语言处理）来说，分词是一步重要的工作,这里使用jieba分词
# ##对你输入的文章进行分词然后统计等等操作
# import jieba
# import numpy as np
# from PIL import Image
# from matplotlib import pyplot as plt
# ##导入用于用于制作词云图的wordcloud
# from wordcloud import WordCloud, ImageColorGenerator
#
# ##打开刚刚的info.txt,并且把得到的句柄内容复制给content
# with open('info.txt', 'r', encoding="UTF-8") as file1:
#     content = "".join(file1.readlines())
# ##然后使用jieba模块进行对文本分词整理
# content_after = "".join(jieba.cut(content, cut_all=True))
#
# ##font_path
# ##使用worldCloud模块对刚刚整理好的分词信息进行处理.
# ##max_font_size参数是可以调整部分当个词语最大尺寸
# ##max_words是最大可以允许多少个词去组成这个词云图
# ##height高度,width宽度,
# ##background_color背景颜色
# wc = WordCloud(font_path="msyh.ttc", background_color="black", max_words=1000, max_font_size=100,
#                width=1500, height=1500).generate(content)
# ##使用matplotlib的pyplot来进行最后的渲染出图.
# plt.imshow(wc)
# ##目标文件另存为这个名录下
# wc.to_file('wolfcodeTarget.png')


# import jieba
# import numpy as np
# from PIL import Image
# from matplotlib import pyplot as plt
# from wordcloud import WordCloud, ImageColorGenerator
#
# with open('info.txt', 'r', encoding="UTF-8") as file1:
#     content = "".join(file1.readlines())
# content_after = "".join(jieba.cut(content, cut_all=float))
# ##添加的代码,把刚刚你保存好的图片用Image方法打开,
# ##然后用numpy转换了一下
# images = Image.open("wolfcode.png")
# maskImages = np.array(images)
#
# ##修改了一下wordCloud参数,就是把这些数据整理成一个形状,
# ##具体的形状会适应你的图片的.
# wc = WordCloud(font_path="msyh.ttc", background_color="white", max_words=1000, max_font_size=100, width=1500,
#                height=1500, mask=maskImages).generate(content)
# plt.imshow(wc)
#
# wc.to_file('wolfcodeTarget.png')

import matplotlib.pyplot as plt  # 数学绘图库
import jieba  # 分词库
from wordcloud import WordCloud  # 词云库

# 1、读入txt文本数据
text = open(r'M:\text_project_python\python_词云图\info.txt', "r").read()

# 2、结巴分词，默认精确模式。可以添加自定义词典userdict.txt,然后jieba.load_userdict(file_name) ,file_name为文件类对象或自定义词典的路径
# 自定义词典格式和默认词库dict.txt一样，一个词占一行：每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒

cut_text = jieba.cut(text)
result = "/".join(cut_text)  # 必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云
# print(result)

# 3、生成词云图，这里需要注意的是WordCloud默认不支持中文，所以这里需已下载好的中文字库
# 无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'
wc = WordCloud(font_path=r"M:\text_project_python\python_词云图\wolfcode.png", background_color='white', width=800,
               height=600, max_font_size=50,
               max_words=1000)  # ,min_font_size=10)#,mode='RGBA',colormap='pink')
wc.generate(result)
wc.to_file(r"M:\text_project_python\python_词云图\wolf.png")  # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰

# 4、显示图片
plt.figure("词云图")  # 指定所绘图名称
plt.imshow(wc)  # 以图片的形式显示词云
plt.axis("on")  # 关闭图像坐标系
plt.show()