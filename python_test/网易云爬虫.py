import requests
from bs4 import BeautifulSoup

header = {  # 伪造浏览器头部
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36', }
link = "https://music.163.com/discover/toplist?id=2250011882"  # 这是网易云音乐链接
r = requests.get(link, headers=header)  # 通过 requests 模块的 get 方法获取网页数据
html = r.content  # 获取网页内容
soup = BeautifulSoup(html, "html.parser")  # 通过 BeautifulSoup 模块解析网页
songs = soup.find("ul", class_="f-hide").select("a",
                                                limit=50)  # 通过分析网页源代码发现排行榜中的歌曲信息全部放在类名称为 f-hide 的 ul 中。

i = 1  # 设置一个自增参数，表示歌曲的数目

for s in songs:  # 遍历输出数组 songs 中的内容
    song_id = s['href'][50:]  # 只截取歌曲链接中的 ID 部分。
    song_name = s.text  # 获取标签歌曲的名称。
    song_down_link = "http://music.163.com/song/media/outer/url?id=" + song_id + ".mp3"
    print("第 " + str(i) + " 首歌曲：" + song_down_link)
    print("正在下载...")

    response = requests.get(song_down_link, headers=header).content  # 亲测必须要加 headers 信息，不然获取不了。
    f = open(song_name + ".mp3", 'wb')  # 写文件 二进制
    f.write(response)
    f.close()
    print("下载完成.\n\r")
    i = i + 1
