import os
import re
import subprocess
import time
from sys import prefix

import pymysql

# # 数据库信息
# host = 'gitlab.galaiot.cn'
# user = 'root'
# password = '123456'
# port = 8889
# db = 'renren'
# # 表前缀(如果没有就留空)
# prefix = 'xh_'

logpath = os.getcwd() + '/mysql.log'


def connectMySQL():
    # 开始连接数据库
    connect = pymysql.connect(
        host='gitlab.galaiot.cn',
        user='root',
        passwd='123456',
        port=3306,
        db='renren',
        charset='utf8'
    )
    # 获取游标
    cur = connect.cursor()
    # 开启mysql标准日志
    cur.execute('set global general_log = on')
    connect.commit()
    currentPath = 'set global log_output = \'file\''
    cur.execute(currentPath)
    connect.commit()
    cur.execute('set global general_log_file=' + '\'' + logpath + '\'')
    connect.commit()
    connect.close()


def monitor():
    command = 'tail -f ' + logpath
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    try:
        while True:
            line = popen.stdout.readline().strip()
            encodeStr = bytes.decode(line)
            pattern = re.findall('Query\s*(.*)', encodeStr, re.S)
            if len(pattern) != 0:
                selectStr = pattern[0]
                if selectStr != "COMMIT":
                    joinTime = time.strftime("%H:%M:%S", time.localtime()) + '    '
                    if prefix != "":
                        reg = re.findall(r'\b' + prefix + '\w*', encodeStr, re.S)
                        if len(reg) != 0:
                            table = '操作的表:' + reg[0]
                            joinTime += table
                    print(joinTime + '   ' + selectStr)

    except KeyboardInterrupt:
        os.remove(logpath)


if __name__ == '__main__':
    connectMySQL()
    time.sleep(1)
    monitor()
